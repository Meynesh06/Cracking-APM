# Spark drawing helpers for the Excalidraw Scene API (scene.py).  Use from tools/diagrams_lN.py:
#   from scene import Scene, INK
#   from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw
#   from shelp import *
# Colours for box fills: 'blue' 'green' 'orange' 'purple' 'red' 'yellow' 'teal' 'pink' 'grey' (+ zones 'zblue' 'zpurple' 'zgreen').
from scene import INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw


def part(s, x, y, label, rows=(), color='blue', w=120, row_h=22, fs=16, label_fs=17):
    """A partition: a labelled box with its rows listed in mono font. Returns the box height."""
    h = 34 + max(1, len(rows)) * row_h + 8
    s.box(x, y, w, h, None, color, opacity=70)
    s.text(x + 10, y + 7, label, label_fs, INK)
    for i, r in enumerate(rows):
        s.text(x + 12, y + 36 + i * row_h, str(r), fs, INK, ff=3)
    return h


def executor(s, x, y, w, h, title, color='zblue', fs=18):
    """An executor (or node / container) as a dashed zone with a title in the top-left corner."""
    s.zone(x, y, w, h, color)
    s.text(x + 10, y + 6, title, fs, INK)


def opnode(s, x, y, name, detail='', color='blue', w=None, fs=17, dfs=14):
    """A query-plan operator box: bold name and an optional detail line (mono). Returns (x, y, w, h)."""
    lines = [l for l in detail.split('\n') if l] if detail else []
    w = w or max(160, _tw(name, fs) + 30, *[_tw(l, dfs, .62) + 24 for l in lines] or [0])
    h = 34 + len(lines) * (dfs + 6) + (6 if lines else 0)
    s.box(x, y, w, h, None, color, opacity=75)
    s.text(x + 12, y + 7, name, fs, INK)
    for i, l in enumerate(lines):
        s.text(x + 12, y + 32 + i * (dfs + 6), l, dfs, INK, ff=3)
    return x, y, w, h


def down(s, x, y1, y2, color=GREY, label=None, fs=14):
    """A vertical arrow from (x, y1) to (x, y2), optional label to its right."""
    s.arrow([(x, y1), (x, y2)], color=color, sw=2)
    if label:
        s.text(x + 8, (y1 + y2) / 2 - fs / 2, label, fs, color)


def right(s, x1, x2, y, color=GREY, label=None, fs=14):
    s.arrow([(x1, y), (x2, y)], color=color, sw=2)
    if label:
        s.text((x1 + x2) / 2 - _tw(label, fs) / 2, y - fs - 6, label, fs, color)


def plan_column(s, x, y, ops, gap=26, color='blue', w=None):
    """Draw operators bottom-up like a physical plan read from the bottom: ops[0] is drawn at the BOTTOM.
    ops = [(name, detail, color?)...]. Returns list of (x, y, w, h) from bottom to top."""
    boxes, sizes = [], []
    for op in ops:
        name, detail = op[0], op[1] if len(op) > 1 else ''
        lines = [l for l in detail.split('\n') if l]
        sizes.append(34 + len(lines) * 20 + (6 if lines else 0))
    total = sum(sizes) + gap * (len(ops) - 1)
    cy = y + total
    for op, h in zip(ops, sizes):
        cy -= h
        b = opnode(s, x, cy, op[0], op[1] if len(op) > 1 else '', op[2] if len(op) > 2 else color, w=w)
        boxes.append(b)
        cy -= gap
    for a, b in zip(boxes, boxes[1:]):            # arrows upwards
        down(s, a[0] + 30, a[1], b[1] + b[3] + 2, GREY)
    return boxes


def memory_stack(s, x, y, w, sections, fs=17, nfs=15):
    """Stacked memory regions top-down: sections = [(label, height, color, note)]. Notes are written to the right."""
    cy = y
    for label, h, color, note in sections:
        s.box(x, cy, w, h, None, color, opacity=70)
        s.text(x + 12, cy + h / 2 - fs / 2 - 2, label, fs, INK)
        if note:
            s.text(x + w + 16, cy + h / 2 - nfs / 2 - 2, note, nfs, GREY, ff=3)
        cy += h
    return cy


def cores(s, x, y, n, busy=(), w=46, h=34, gap=8, fs=15):
    """A row of CPU cores; indexes in `busy` are drawn green (working), others grey (idle)."""
    for i in range(n):
        s.box(x + i * (w + gap), y, w, h, f'c{i}', 'green' if i in busy else 'grey', fs=fs, ff=3)


def legend(s, x, y, items, fs=15):
    """items = [(color_name, text)] small swatches with text."""
    for i, (c, t) in enumerate(items):
        s.box(x, y + i * 26, 18, 18, None, c)
        s.text(x + 26, y + i * 26 - 1, t, fs, INK)


def title(s, text, sub=None, color=PURPLE):
    s.text(0, 0, text, 24, color)
    if sub:
        s.text(0, 34, sub, 17, GREY)
