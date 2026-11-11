# Refresh ```output blocks from the real run (review the diff it prints!).
# Usage: python3 fixout.py notes/parts/lN.src.md [--write]
# Without --write it only reports; with --write it rewrites mismatching ```output blocks (error blocks are never touched).
import re, sys, subprocess, tempfile, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runner as spark_run
FENCE = re.compile(r'^```(\w+)([^\n]*)\n(.*?)^```\s*$', re.S | re.M)
path = sys.argv[1]; write = '--write' in sys.argv
text = open(path).read()
blocks = list(FENCE.finditer(text))
out_text, pos = [], 0
changed = 0
norm = lambda t: '\n'.join(l.rstrip() for l in t.rstrip('\n').split('\n'))
for i, m in enumerate(blocks):
    if m.group(1) != 'python' or 'nocheck' in m.group(2):
        continue
    nxt = blocks[i + 1] if i + 1 < len(blocks) else None
    if not nxt or nxt.group(1) != 'output' or text[m.end():nxt.start()].strip():
        continue
    class R: pass
    r = R(); r.stdout, r.stderr = spark_run.run(m.group(3))
    chain, k, endp = [], i + 1, m.end()
    while k < len(blocks) and blocks[k].group(1) in ('output', 'error') and not text[endp:blocks[k].start()].strip():
        chain.append(blocks[k]); endp = blocks[k].end(); k += 1
    if r.stderr.strip() and not any(b.group(1) == 'error' for b in chain):
        print(f'!! line {text[:m.start()].count(chr(10))+1}: stderr\n{r.stderr[-300:]}')
    if norm(r.stdout) != norm(nxt.group(3)):
        changed += 1
        line = text[:nxt.start()].count('\n') + 1
        print(f'-- output block at line {line} differs:\nEXPECTED:\n{nxt.group(3)}GOT:\n{r.stdout}')
        ws = re.search(r'\s*$', text[nxt.start():nxt.end()]).group(0)          # keep the blank line(s) after the closing fence
        out_text.append((nxt.start(), nxt.end(), '```output\n' + r.stdout.rstrip('\n') + '\n```' + ws))
if write and out_text:
    for a, b, new in sorted(out_text, reverse=True):
        text = text[:a] + new + text[b:]
    open(path, 'w').write(text)
    print('rewrote', len(out_text), 'output blocks')
print('mismatching output blocks:', changed)
