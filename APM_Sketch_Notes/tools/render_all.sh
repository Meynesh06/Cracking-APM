#!/bin/sh
# Re-run every tools/diagrams_*.py and render all diagrams (after a toolkit or helper change).
set -e
cd "$(dirname "$0")"
for f in diagrams_*.py; do [ -f "$f" ] && python3 "$f" ../diagrams/src; done
node render-diagrams.mjs ../diagrams/src ../diagrams/out | tail -3
