"""Transcript utilities for YouTube-style auto transcripts (the "Show transcript" panel, copied as text).

Input format: lines of timestamps ("0:00", "1:02:03"), optional spoken-time lines ("8 seconds", "1 minute, 2 seconds"),
text lines, and optional chapter lines ("Chapter 3: Lack of ACID Support"). Several videos pasted one after another
(timestamps restart at 0:00) are handled by `playlist`.

  python3 transcript.py clean    RAW.md CLEAN.md            drop the spoken-time lines (keeps timestamps + chapters)
  python3 transcript.py chapters CLEAN.md                   list chapters: number, start, words, minutes (to plan parts)
  python3 transcript.py split    CLEAN.md PLAN OUTDIR       write OUTDIR/p01.md ... one file per part (internal files: timestamps kept)
           PLAN = "1-9,10-11,12-13"  (chapter ranges per part, in order)  or  "@0:00,@36:00,@1:10:00" (start times, no chapters)
  python3 transcript.py playlist RAW.md OUTDIR              a paste of several videos -> OUTDIR/t01.md, t02.md ... (split where time restarts)
  python3 transcript.py md       CLEAN.md PLAN OUT.md --title "..." [--intro "..."] [--parts "Title 1|Title 2|..."]
           readable transcript for the reader: no timestamps, joined into paragraphs, grouped by part and chapter
  python3 transcript.py words    FILE.md                    word count and an estimate of the spoken minutes
"""
import re, sys, os

TS = re.compile(r'^\s*(\d{1,2}:)?\d{1,2}:\d\d\s*$')
SPOKEN = re.compile(r'^\s*(\d+ hours?,?\s*)?(\d+ minutes?,?\s*)?(\d+ seconds?)?\s*$')
CHAP = re.compile(r'^\s*Chapter\s+(\d+)\s*[:.\-–]\s*(.+?)\s*$', re.I)


def secs(t):
    s = 0
    for p in t.strip().split(':'):
        s = s * 60 + int(p)
    return s


def is_spoken(l):
    return bool(l.strip()) and bool(SPOKEN.match(l)) and any(w in l for w in ('second', 'minute', 'hour'))


def parse(path):
    """-> list of (chapter_no or None, chapter_title, [(t_seconds, text), ...]) in order."""
    chaps, cur, t = [], [None, '', []], 0
    for raw in open(path, encoding='utf-8'):
        l = raw.rstrip('\n')
        if not l.strip() or is_spoken(l):
            continue
        m = CHAP.match(l)
        if m:
            if cur[2] or cur[0] is not None:
                chaps.append(tuple(cur))
            cur = [int(m.group(1)), m.group(2), []]
            continue
        if TS.match(l):
            t = secs(l)
            continue
        cur[2].append((t, l.strip()))
    chaps.append(tuple(cur))
    return [c for c in chaps if c[2] or c[0] is not None]


def fmt(s):
    return f'{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}' if s >= 3600 else f'{s // 60}:{s % 60:02d}'


def cmd_clean(raw, out):
    keep = [l for l in open(raw, encoding='utf-8').read().split('\n') if not is_spoken(l)]
    open(out, 'w', encoding='utf-8').write('\n'.join(keep))
    print(out, len(keep), 'lines')


def cmd_chapters(path):
    total = 0
    for no, title, lines in parse(path):
        w = sum(len(x.split()) for _, x in lines)
        total += w
        start = fmt(lines[0][0]) if lines else '-'
        print(f'{str(no):>3}  {start:>8}  {w:6} words  ~{w / 150:4.1f} min  {title}')
    print(f'total {total} words, about {total / 150:.0f} spoken minutes')


def plan_parts(chaps, plan):
    """-> list of lists of chapter tuples (one list per part)."""
    if plan.startswith('@'):
        starts = [secs(x.lstrip('@')) for x in plan.split(',')]
        lines = [(t, x, no, title) for no, title, ls in chaps for t, x in ls]
        parts = []
        for i, s in enumerate(starts):
            e = starts[i + 1] if i + 1 < len(starts) else 10 ** 9
            sel = [l for l in lines if s <= l[0] < e]
            groups, last = [], object()
            for t, x, no, title in sel:
                if (no, title) != last:
                    groups.append((no, title, [])); last = (no, title)
                groups[-1][2].append((t, x))
            parts.append(groups)
        return parts
    by_no = {c[0]: c for c in chaps}
    parts = []
    for rng in plan.split(','):
        a, _, b = rng.partition('-')
        parts.append([by_no[n] for n in range(int(a), int(b or a) + 1) if n in by_no])
    return parts


def cmd_split(path, plan, outdir):
    os.makedirs(outdir, exist_ok=True)
    for i, part in enumerate(plan_parts(parse(path), plan), 1):
        out = []
        for no, title, lines in part:
            if no is not None:
                out.append(f'Chapter {no}: {title}')
            last = None
            for t, x in lines:
                if t != last:
                    out.append(fmt(t)); last = t
                out.append(x)
        f = os.path.join(outdir, f'p{i:02d}.md')
        open(f, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
        print(f, sum(len(x.split()) for c in part for _, x in c[2]), 'words')


def cmd_playlist(raw, outdir):
    os.makedirs(outdir, exist_ok=True)
    vids, cur, last = [], [], -1
    for l in open(raw, encoding='utf-8').read().split('\n'):
        if is_spoken(l):
            continue
        if TS.match(l):
            t = secs(l)
            if t < last - 30 and cur:          # time went back: a new video starts
                vids.append(cur); cur = []
            last = t
        cur.append(l)
    if cur:
        vids.append(cur)
    for i, v in enumerate(vids, 1):
        f = os.path.join(outdir, f't{i:02d}.md')
        open(f, 'w', encoding='utf-8').write('\n'.join(v).strip() + '\n')
        print(f, sum(len(x.split()) for x in v if not TS.match(x)), 'words')


def paragraphs(text, target=85):
    sents = re.split(r'(?<=[.!?])\s+', re.sub(r'\s+', ' ', text).strip())
    out, cur, n = [], [], 0
    for s in sents:
        cur.append(s); n += len(s.split())
        if n >= target:
            out.append(' '.join(cur)); cur, n = [], 0
    if cur:
        out.append(' '.join(cur))
    return out


def cmd_md(path, plan, out, title, intro='', part_titles=None):
    doc = [f'# {title}', '']
    if intro:
        doc += [intro, '']
    parts = plan_parts(parse(path), plan)
    for i, part in enumerate(parts, 1):
        pt = part_titles[i - 1] if part_titles and i - 1 < len(part_titles) else ''
        doc += [f'## Part {i}' + (f' · {pt}' if pt else ''), '']
        for no, ctitle, lines in part:
            if no is not None:
                doc += [f'### Chapter {no} · {ctitle}', '']
            doc += [p + '\n' for p in paragraphs(' '.join(x for _, x in lines))]
    open(out, 'w', encoding='utf-8').write('\n'.join(doc).rstrip() + '\n')
    print(out, len(parts), 'parts')


def cmd_words(path):
    w = sum(len(l.split()) for l in open(path, encoding='utf-8') if not TS.match(l) and not is_spoken(l))
    print(f'{w} words, about {w / 150:.0f} spoken minutes')


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a:
        print(__doc__); sys.exit()
    cmd = a[0]
    if cmd == 'clean': cmd_clean(a[1], a[2])
    elif cmd == 'chapters': cmd_chapters(a[1])
    elif cmd == 'split': cmd_split(a[1], a[2], a[3])
    elif cmd == 'playlist': cmd_playlist(a[1], a[2])
    elif cmd == 'words': cmd_words(a[1])
    elif cmd == 'md':
        opt = lambda k: a[a.index(k) + 1] if k in a else ''
        cmd_md(a[1], a[2], a[3], opt('--title') or 'Transcript', opt('--intro'), opt('--parts').split('|') if opt('--parts') else None)
    else:
        print(__doc__)
