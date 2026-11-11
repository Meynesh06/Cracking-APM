# Contact sheet of rendered diagrams, two per row:  python3 sheet.py PREFIX out.html   (e.g. PREFIX = l7-)
# then:  node shot.mjs file:///abs/out.html /abs/out.png 1280 800   and Read the PNG.
import sys, glob, os
pre, out = sys.argv[1], sys.argv[2]
d = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'diagrams', 'out'))
files = sorted(glob.glob(os.path.join(d, f'{pre}*.svg')))
html = ['<html><body style="margin:0;background:#fff;font:14px sans-serif;display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:10px">']
for f in files:
    html.append(f'<div style="border:1px solid #ccc;padding:6px"><b>{os.path.basename(f)}</b><img src="file://{f}" style="width:100%"></div>')
html.append('</body></html>')
os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
open(out, 'w').write('\n'.join(html))
print(len(files), 'diagrams ->', out)
