#!/bin/sh
# Merge every page into notes/<slug>_Notes.md, build traces, check every code block, build dist/<slug>_Notes.html.
# (Diagrams are rendered per page by lchk.sh; run `sh tools/render_all.sh` to re-render all of them.)
set -e
cd "$(dirname "$0")"
SLUG=$(python3 -c "import json;print(json.load(open('../dkfile.json'))['slug'])")
cd ../notes/parts
for f in l*.src.md; do python3 ../../tools/ts.py "$f" "${f%.src.md}.md" >/dev/null; done
cd ..
{ cat parts/intro.md; for n in $(ls parts | grep -E '^l[0-9]+\.md$' | sed 's/^l\([0-9]*\)\.md$/\1/' | sort -n); do printf '\n\n'; cat parts/l$n.md; done; } > ${SLUG}_Notes.md
cd ../tools
mkdir -p ../dist
python3 make_traces.py ../notes/${SLUG}_Notes.md
python3 check_code.py ../notes/${SLUG}_Notes.md
node build.mjs ../notes/${SLUG}_Notes.md ../diagrams/out template.html ../dist/${SLUG}_Notes.html
