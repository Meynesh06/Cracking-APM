# Delta Lake drawing helpers for the Excalidraw Scene API (scene.py).  Use from tools/diagrams_lN.py:
#   from scene import Scene, INK
#   from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw
#   from shelp import legend, title, down, right, part, cores, executor
#   from dlhelp import *
# Colour language (keep it the same on every page):
#   blue   = Parquet data files at rest        purple = _delta_log commits (JSON) and titles
#   orange = checkpoints / compaction / shuffle / network transfer
#   green  = active file, good result, committed       red = removed / tombstoned / problem / conflict
#   yellow = highlighted row or key (the row being changed)   grey = inactive, ignored, orphaned
#   teal   = metadata / catalog (Unity Catalog, metastore)     pink = deletion vectors (bitmaps)
from scene import INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw

PINK = '#9c36b5'


def pfile(s, x, y, name, rows=(), color='blue', w=150, row_h=21, fs=15, name_fs=16, crossed=False, note=None):
    """A Parquet data file: file name on top, its rows below in mono. Returns the height.
    crossed=True draws it greyed with a red diagonal (a removed / tombstoned file)."""
    h = 32 + max(1, len(rows)) * row_h + 8 if rows else 44
    s.box(x, y, w, h, None, 'grey' if crossed else color, opacity=60 if crossed else 75)
    s.text(x + 10, y + 7, name, name_fs, GREY if crossed else INK, ff=3)
    for i, r in enumerate(rows):
        s.text(x + 12, y + 33 + i * row_h, str(r), fs, GREY if crossed else INK, ff=3)
    if crossed:
        s.line([(x + 6, y + h - 6), (x + w - 6, y + 6)], color=RED, sw=3)
    if note:
        s.text(x, y + h + 6, note, 14, GREY)
    return h


def commit(s, x, y, name, actions=(), w=260, fs=15, name_fs=16, color='purple'):
    """A _delta_log JSON commit card. actions = ['add f2.parquet', 'remove f1.parquet', 'commitInfo UPDATE' ...]:
    lines starting with 'add' are green with '+', 'remove' red with '-', anything else grey. Returns the height."""
    h = 32 + max(1, len(actions)) * (fs + 7) + 8
    s.box(x, y, w, h, None, color, opacity=55)
    s.text(x + 10, y + 7, name, name_fs, INK, ff=3)
    for i, a in enumerate(actions):
        c = GREEN if a.startswith('add') else RED if a.startswith('remove') else GREY
        mark = '+ ' if a.startswith('add') else '- ' if a.startswith('remove') else '  '
        s.text(x + 12, y + 33 + i * (fs + 7), mark + a, fs, c, ff=3)
    return h


def ckpt(s, x, y, name='00010.checkpoint.parquet', note=None, w=None, fs=15):
    """A checkpoint file (orange): the whole table state up to that version, in Parquet."""
    w = w or max(200, _tw(name, fs, .62) + 24)
    s.box(x, y, w, 44, None, 'orange', opacity=75)
    s.text(x + 10, y + 12, name, fs, INK, ff=3)
    if note:
        s.text(x, y + 52, note, 14, ORANGE)
    return 44


def dv(s, x, y, nbits=8, ones=(), label='deletion vector', cell=24, fs=14):
    """A deletion-vector bitmap: a row of cells, the positions in `ones` set to 1 (pink). Returns the width."""
    s.text(x, y - 22, label, fs, PINK)
    for i in range(nbits):
        on = i in ones
        s.box(x + i * cell, y, cell, cell, '1' if on else '0', 'pink' if on else 'grey', fs=13, ff=3, opacity=80 if on else 50)
    return nbits * cell


def folder(s, x, y, w, h, name, color='zblue', fs=17):
    """A storage folder (table directory, container, bucket) as a dashed zone with its path on top."""
    s.zone(x, y, w, h, color)
    s.text(x + 10, y + 6, name, fs, INK, ff=3)


def versions(s, x, y, labels, gap=150, color='purple', fs=16, w=110, h=40, current=None):
    """A horizontal version timeline: boxes v0, v1 ... with arrows. labels = ['v0 CREATE', 'v1 INSERT' ...].
    `current` = index drawn green (the table's latest version or the one being read). Returns the right edge."""
    for i, t in enumerate(labels):
        bx = x + i * gap
        s.box(bx, y, w, h, t, 'green' if i == current else color, fs=fs, opacity=70)
        if i:
            s.arrow([(bx - gap + w + 4, y + h / 2), (bx - 4, y + h / 2)], color=GREY)
    return x + (len(labels) - 1) * gap + w


def rowtable(s, x, y, header, rows, colw=None, fs=15, row_h=26, hl=(), struck=(), color='blue'):
    """A small table drawn as boxes: header row purple, data rows in mono. hl = row indexes to highlight (yellow),
    struck = row indexes drawn grey with a red strike line. Returns (width, height)."""
    colw = colw or [max(70, _tw(str(c), fs, .62) + 22) for c in header]
    W = sum(colw)
    s.box(x, y, W, row_h, None, 'purple', opacity=55)
    cx = x
    for c, cw in zip(header, colw):
        s.text(cx + 8, y + 4, str(c), fs, INK, ff=3)
        cx += cw
    for r, row in enumerate(rows):
        ry = y + row_h * (r + 1)
        col = 'yellow' if r in hl else 'grey' if r in struck else color
        s.box(x, ry, W, row_h, None, col, opacity=45)
        cx = x
        for c, cw in zip(row, colw):
            s.text(cx + 8, ry + 4, str(c), fs, GREY if r in struck else INK, ff=3)
            cx += cw
        if r in struck:
            s.line([(x + 4, ry + row_h / 2), (x + W - 4, ry + row_h / 2)], color=RED, sw=2)
    return W, row_h * (len(rows) + 1)


def note(s, x, y, text, color=GREY, fs=15):
    """A grey hand-written side note (split long text yourself: one line <= ~60 characters)."""
    for i, line in enumerate(text.split('\n')):
        s.text(x, y + i * (fs + 6), line, fs, color)
