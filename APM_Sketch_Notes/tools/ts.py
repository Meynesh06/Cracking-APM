# Expand @[m:ss] / @[h:mm:ss] shorthand into YouTube timestamp links.
# Usage: python3 ts.py src.md out.md   (video id read from the <!-- lecture ... video="..." --> comment)
import re, sys

src, out = sys.argv[1], sys.argv[2]
text = open(src).read()
m1 = re.search(r'video="([\w-]+)"', text)
vid = m1.group(1) if m1 else None          # a lecture rebuilt from notebooks has no video
m2 = re.search(r'video2="([\w-]+)"', text)
vid2 = m2.group(1) if m2 else None

def secs(t):
    s = 0
    for part in t.split(':'):
        s = s * 60 + int(part)
    return s

# @[m:ss] -> first video, @B[m:ss] -> second video (lectures made of two videos)
def link(m):
    v = vid2 if m.group(1) == 'B' else vid
    if v is None and m.group(1) == 'B':
        raise SystemExit('@B timestamp but no video2 in the lecture comment')
    if v is None:                     # video link not known yet: an exact time, without a link
        return f'<span class="ts nolink" title="video link pending">{m.group(2)}</span>'
    return f'[{m.group(2)}](https://www.youtube.com/watch?v={v}&t={secs(m.group(2))}s)'

text = re.sub(r'@(B)?\[(\d+(?::\d\d){1,2})\]', link, text)
open(out, 'w').write(text)
print(out, 'timestamps:', len(re.findall(r'&t=\d+s\)|class="ts nolink"', text)))
