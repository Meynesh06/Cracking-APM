# Shared drawing helpers for the lecture scenes (arrays, stacks, circles of people).
import math
from scene import INK

RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY = '#e03131', '#2f9e44', '#1971c2', '#7048e8', '#e8590c', '#0c8599', '#868e96'


def arr(s, x, y, vals, color='blue', w=46, h=46, fs=20, hi=None, cross=None, ff=3):
    """A row of cells. hi / cross: an index (or a set of indexes) to highlight / strike out."""
    his = hi if isinstance(hi, (set, list, tuple)) else ({hi} if hi is not None else set())
    crs = cross if isinstance(cross, (set, list, tuple)) else ({cross} if cross is not None else set())
    for i, v in enumerate(vals):
        s.box(x + i * w, y, w, h, str(v), 'yellow' if i in his else color, fs=fs, ff=ff)
        if i in crs:
            s.line([(x + i * w + 5, y + 5), (x + i * w + w - 5, y + h - 5)], color=RED, sw=3)
    return x + len(vals) * w


def stack(s, x, ybase, vals, color='orange', w=70, h=40, fs=20, hi=None, cross=None, top_label=True,
          caption=None, cap_color=INK, ghost=None):
    """A vertical stack drawn bottom → top, standing on a base line at ybase. vals are bottom → top.
    ghost: an index drawn dashed (a slot that is empty for now)."""
    his = hi if isinstance(hi, (set, list, tuple)) else ({hi} if hi is not None else set())
    crs = cross if isinstance(cross, (set, list, tuple)) else ({cross} if cross is not None else set())
    s.line([(x - 12, ybase + 3), (x + w + 12, ybase + 3)], sw=4)
    for i, v in enumerate(vals):
        y = ybase - (i + 1) * h
        c = 'yellow' if i in his else color
        s.box(x, y, w, h, str(v), c, fs=fs, ff=3, dashed=(ghost == i))
        if i in crs:
            s.line([(x + 6, y + 5), (x + w - 6, y + h - 5)], color=RED, sw=3)
    if top_label and vals:
        ty = ybase - len(vals) * h + h / 2 - 11
        s.text(x + w + 10, ty, "← top", 16, GREY)
    if not vals:
        s.text(x + 6, ybase - 30, "empty", 16, GREY)
    if caption:
        s.text(x - 10, ybase + 14, caption, 16, cap_color)
    return ybase - len(vals) * h


def circle_people(s, cx, cy, r, people, dead=(), hi=None, fs=18, size=46, order=None):
    """People numbered around a circle, clockwise from the top. dead: crossed out. order: {p: '①'} labels."""
    n = len(people)
    pos = {}
    for i, p in enumerate(people):
        a = -math.pi / 2 + 2 * math.pi * i / n
        px, py = cx + r * math.cos(a), cy + r * math.sin(a)
        pos[p] = (px, py)
        c = 'grey' if p in dead else ('yellow' if p == hi else 'blue')
        s.box(px - size / 2, py - size / 2, size, size, str(p), c, fs=fs, ff=3, shape='ellipse')
        if p in dead:
            s.line([(px - size / 2 + 6, py - size / 2 + 6), (px + size / 2 - 6, py + size / 2 - 6)], color=RED, sw=3)
        if order and p in order:
            ox, oy = cx + (r + 42) * math.cos(a), cy + (r + 42) * math.sin(a)
            s.text(ox - 10, oy - 12, order[p], 18, RED)
    return pos


# ───────────────────────── binary-search helpers ─────────────────────────
def _tw(txt, fs, k=0.56):
    return len(txt) * fs * k


def bs_row(s, x, y, vals, lo=None, hi=None, mid=None, res=None, found=None, w=50, h=48, fs=20, ff=3,
           idx=True, ptr=True, color='blue', dead_color='grey', cross=None, lo_name='lo', hi_name='hi',
           mid_name='mid', mark=None, idx_fs=14, ptr_fs=16):
    """An array as binary search sees it.
    cells outside [lo, hi] are drawn dead (grey, hatched); mid is yellow; res (best candidate) and found are green.
    idx: index numbers above; ptr: lo / mid / hi labels with little arrows below.
    mark: {index: 'red'|'green'|...} force a colour. cross: indexes struck out.
    Returns the x just after the last cell."""
    n = len(vals)
    lo_ = 0 if lo is None else lo
    hi_ = n - 1 if hi is None else hi
    crs = cross if isinstance(cross, (set, list, tuple)) else ({cross} if cross is not None else set())
    mark = mark or {}
    for i, v in enumerate(vals):
        cx = x + i * w
        live = lo_ <= i <= hi_
        if i in mark:
            c, style, op = mark[i], 'solid', 100
        elif found is not None and i == found:
            c, style, op = 'green', 'solid', 100
        elif res is not None and i == res:
            c, style, op = 'green', 'solid', 100
        elif mid is not None and i == mid and live:
            c, style, op = 'yellow', 'solid', 100
        elif live:
            c, style, op = color, 'solid', 100
        else:
            c, style, op = dead_color, 'hachure', 70
        s.box(cx, y, w, h, str(v), c, fs=fs, ff=ff, style=style, opacity=op)
        if idx:
            t = str(i)
            s.text(cx + w / 2 - _tw(t, idx_fs) / 2, y - idx_fs - 8, t, idx_fs, GREY, ff=3)
        if i in crs:
            s.line([(cx + 5, y + 5), (cx + w - 5, y + h - 5)], color=RED, sw=3)
    if ptr:
        groups = {}
        for nm, val, col in ((lo_name, lo, BLUE), (mid_name, mid, ORANGE), (hi_name, hi, PURPLE)):
            if val is not None and 0 <= val < n:
                groups.setdefault(val, []).append((nm, col))
            elif val is not None:                                  # a pointer that left the array
                groups.setdefault(max(-1, min(val, n)), []).append((nm, col))
        for i, lst in groups.items():
            cx = x + i * w + w / 2
            if i < 0:
                cx = x - 16
            elif i >= n:
                cx = x + n * w + 16
            label = '/'.join(nm for nm, _ in lst)
            col = lst[0][1] if len(lst) == 1 else INK
            s.arrow([(cx, y + h + 34), (cx, y + h + 6)], color=col, sw=2)
            s.text(cx - _tw(label, ptr_fs) / 2, y + h + 36, label, ptr_fs, col, ff=3)
    return x + n * w


def numline(s, x, y, length, lo, hi, marks=(), h=14, fs=16, lo_txt=None, hi_txt=None, ok=None, bad=None):
    """A number line from lo to hi (values), drawn length px wide. marks: [(value, label, color)].
    ok / bad: (a, b) value ranges painted green / red under the line."""
    def px(v):
        return x + (v - lo) / (hi - lo) * length
    if bad:
        s.box(px(bad[0]), y - h, px(bad[1]) - px(bad[0]), h, None, 'red', opacity=70)
    if ok:
        s.box(px(ok[0]), y - h, px(ok[1]) - px(ok[0]), h, None, 'green', opacity=70)
    s.line([(x, y), (x + length, y)], sw=3)
    for v, lab, col in [(lo, lo_txt or str(lo), INK), (hi, hi_txt or str(hi), INK)] + list(marks):
        s.line([(px(v), y - 9), (px(v), y + 9)], color=INK, sw=2)
        s.text(px(v) - _tw(lab, fs) / 2, y + 14, lab, fs, col, ff=3)
    return px
