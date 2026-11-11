# Package the deliverables: <slug>_Notes.html, <slug>_Notes.md (clean), <slug>_Transcript.md (if present) and a bundle zip
# (markdown + html + transcript + every used diagram as .svg and .excalidraw + screenshots + the lab helpers).
# Output folder: $DKFILE_OUT, else /mnt/user-data/outputs when it exists (Claude cloud sessions), else <project>/release.
# Usage: python3 tools/package.py
import json, os, re, shutil, zipfile

R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
CFG = json.load(open(os.path.join(R, 'dkfile.json')))
SLUG = CFG['slug']
OUT = os.environ.get('DKFILE_OUT') or ('/mnt/user-data/outputs' if os.path.isdir('/mnt/user-data/outputs') else os.path.join(R, 'release'))
PK = os.path.join(R, 'release', f'{SLUG}_Notes')
shutil.rmtree(PK, ignore_errors=True)
os.makedirs(os.path.join(PK, 'diagrams'))
md = open(os.path.join(R, 'notes', f'{SLUG}_Notes.md'), encoding='utf-8').read()
md = re.sub(r'^<!-- check: [^>]*-->\n', '', md, flags=re.M)
md = re.sub(r'^(```\w+[^\n]*?) nocheck', r'\1', md, flags=re.M)


def tracer(m):
    call = re.search(r'data-call="([^"]+)"', m.group(0)).group(1)
    return f'> ▶ **Step-through:** in the HTML version you can run `{call}` one step at a time and watch the call stack.'


md = re.sub(r'<div class="tracer"[^>]*></div>', tracer, md)
md = md.replace('<!-- hero: ', '<!-- ')
open(os.path.join(PK, f'{SLUG}_Notes.md'), 'w', encoding='utf-8').write(md)
shutil.copy(os.path.join(R, 'dist', f'{SLUG}_Notes.html'), PK)
files = [f'{SLUG}_Notes.html', f'{SLUG}_Notes.md']
tr = os.path.join(R, f'{SLUG}_Transcript.md')
if os.path.exists(tr):
    shutil.copy(tr, PK); files.append(f'{SLUG}_Transcript.md')
used = sorted(set(re.findall(r'diagrams/([\w-]+)\.svg', md)))
shots = sorted(set(re.findall(r'shots/([\w.-]+\.(?:webp|png|jpe?g))', md)))
if shots:
    os.makedirs(os.path.join(PK, 'shots'))
    for s in shots:
        shutil.copy(os.path.join(R, 'diagrams', 'shots', s), os.path.join(PK, 'shots'))
if os.path.isdir(os.path.join(R, 'lab')):
    shutil.copytree(os.path.join(R, 'lab'), os.path.join(PK, 'lab'), ignore=shutil.ignore_patterns(
        'data', 'out', '__pycache__', '_blk_*', 'spark-warehouse', 'derby*', 'metastore_db', '.venv'))
for d in used:
    for ext in ('.svg', '.excalidraw'):
        shutil.copy(os.path.join(R, 'diagrams', 'out', d + ext), os.path.join(PK, 'diagrams'))
zp = os.path.join(R, 'release', f'{SLUG}_Notes_bundle.zip')
with zipfile.ZipFile(zp, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, _, fs in os.walk(PK):
        for f in sorted(fs):
            p = os.path.join(root, f)
            z.write(p, os.path.relpath(p, os.path.dirname(PK)))
os.makedirs(OUT, exist_ok=True)
for f in files:
    shutil.copy(os.path.join(PK, f), OUT)
shutil.copy(zp, OUT)
print('diagrams:', len(used), '| files in bundle:', sum(len(f) for _, _, f in os.walk(PK)), '| out:', OUT)
for f in files + [os.path.basename(zp)]:
    print(f, round(os.path.getsize(os.path.join(OUT, f)) / 1024), 'KB')
