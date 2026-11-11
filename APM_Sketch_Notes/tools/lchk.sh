#!/bin/sh
# Per-page check + preview (safe to run in parallel with other pages).
# Usage: sh tools/lchk.sh N      (N = page number of notes/parts/lN.src.md)
# 1) runs every code block of lN.src.md against its ```output block   2) builds that page's step-through traces
# 3) renders ONLY that page's diagrams (tools/diagrams_lN.py -> diagrams/out/lN-*.svg)
# 4) builds a one-page preview: $PV/pN.html  (default PV=/tmp/dkfile-pv/<project>)
set -e
N=$1
cd "$(dirname "$0")"
P=../notes/parts
PROJ=$(basename "$(cd .. && pwd)")
PV=${PV:-/tmp/dkfile-pv/$PROJ}
python3 ts.py $P/l$N.src.md $P/l$N.md >/dev/null
echo "== code"; python3 check_code.py $P/l$N.src.md
echo "== traces"; python3 make_traces.py $P/l$N.src.md
if [ -f diagrams_l$N.py ]; then
  echo "== diagrams"; python3 diagrams_l$N.py ../diagrams/src; node render-diagrams.mjs ../diagrams/src ../diagrams/out l$N- | tail -40
fi
echo "== preview"; mkdir -p "$PV"
{ cat $P/intro.md; printf '\n\n'; cat $P/l$N.md; } > "$PV/p$N.md"
TRACE_DIR="$(pwd)/../traces" node build.mjs "$PV/p$N.md" ../diagrams/out template.html "$PV/p$N.html"
echo "preview: file://$PV/p$N.html#l$N"
