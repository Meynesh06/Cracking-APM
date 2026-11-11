# Shared Excalidraw skeleton helper
import json, sys, os

OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
os.makedirs(OUT, exist_ok=True)

PAL = {
    'blue':   ('#a5d8ff', '#1971c2'),
    'green':  ('#b2f2bb', '#2f9e44'),
    'orange': ('#ffd8a8', '#e8590c'),
    'purple': ('#d0bfff', '#7048e8'),
    'red':    ('#ffc9c9', '#e03131'),
    'yellow': ('#fff3bf', '#f08c00'),
    'teal':   ('#c3fae8', '#0c8599'),
    'pink':   ('#eebefa', '#9c36b5'),
    'grey':   ('#e9ecef', '#868e96'),
    'zblue':  ('#dbe4ff', '#4263eb'),
    'zpurple':('#e5dbff', '#7048e8'),
    'zgreen': ('#d3f9d8', '#2f9e44'),
}
INK = '#1e1e1e'


class Scene:
    def __init__(self):
        self.els = []
        self.n = 0

    def _id(self, p):
        self.n += 1
        return f'{p}{self.n}'

    def box(self, x, y, w, h, text=None, color='blue', fs=20, style='solid', shape='rectangle',
            dashed=False, sw=2, ff=5, ink=INK, opacity=100, rough=1):
        fill, stroke = PAL[color]
        e = {'type': shape, 'id': self._id('b'), 'x': x, 'y': y, 'width': w, 'height': h,
             'backgroundColor': fill, 'fillStyle': style, 'strokeColor': stroke, 'strokeWidth': sw,
             'roughness': rough, 'opacity': opacity}
        if shape == 'rectangle':
            e['roundness'] = {'type': 3}
        if dashed:
            e['strokeStyle'] = 'dashed'
        if text is not None:
            e['label'] = {'text': text, 'fontSize': fs, 'fontFamily': ff, 'strokeColor': ink}
        self.els.append(e)
        return e

    def zone(self, x, y, w, h, color='zblue'):
        return self.box(x, y, w, h, None, color, style='solid', sw=1, opacity=45, dashed=True)

    def text(self, x, y, s, fs=20, color=INK, ff=5, align='left'):
        e = {'type': 'text', 'id': self._id('t'), 'x': x, 'y': y, 'text': s, 'fontSize': fs,
             'fontFamily': ff, 'strokeColor': color, 'textAlign': align}
        self.els.append(e)
        return e

    def arrow(self, pts, color=INK, dashed=False, end='arrow', start=None, sw=2):
        x0, y0 = pts[0]
        rel = [[px - x0, py - y0] for px, py in pts]
        xs = [p[0] for p in rel]; ys = [p[1] for p in rel]
        e = {'type': 'arrow', 'id': self._id('a'), 'x': x0, 'y': y0,
             'width': max(xs) - min(xs), 'height': max(ys) - min(ys), 'points': rel,
             'strokeColor': color, 'strokeWidth': sw, 'endArrowhead': end, 'startArrowhead': start}
        if dashed:
            e['strokeStyle'] = 'dashed'
        if len(pts) > 2:
            e['roundness'] = None
        self.els.append(e)
        return e

    def line(self, pts, color=INK, dashed=False, sw=2):
        return self.arrow(pts, color, dashed, end=None, start=None, sw=sw)

    def save(self, name):
        with open(os.path.join(OUT, name + '.json'), 'w') as f:
            json.dump(self.els, f)




# ---- tree helper ---------------------------------------------------------
# node = {'t': label, 'k': [children], 'e': edge label (on the edge from the parent), 'c': color, 'w': width}
def _leaves(nd):
    ks = nd.get('k') or []
    return 1 if not ks else sum(_leaves(k) for k in ks)


def tree(s, root, x0, y0, dx=150, dy=130, w=120, h=56, fs=18, ff=5, edge_fs=15, edge_color='#1e1e1e',
         color='blue', leaf_color=None, pos=None):
    """Lay out and draw a tree; leaves are spaced dx apart, levels dy apart. Returns {id(node): (cx, cy)}."""
    pos = {} if pos is None else pos
    counter = [0]

    def place(nd, depth):
        ks = nd.get('k') or []
        if not ks:
            cx = x0 + counter[0] * dx + w / 2
            counter[0] += 1
        else:
            xs = [place(k, depth + 1) for k in ks]
            cx = sum(xs) / len(xs)
        pos[id(nd)] = (cx, y0 + depth * dy)
        return cx

    place(root, 0)

    def draw(nd):
        cx, cy = pos[id(nd)]
        ks = nd.get('k') or []
        c = nd.get('c') or (leaf_color if (not ks and leaf_color) else color)
        ww = nd.get('w', w)
        s.box(cx - ww / 2, cy, ww, h, nd['t'], c, fs=nd.get('fs', fs), ff=nd.get('ff', ff), dashed=nd.get('dashed', False))
        for k in ks:
            kx, ky = pos[id(k)]
            s.arrow([(cx, cy + h + 2), (kx, ky - 3)], color=k.get('ec', edge_color), dashed=k.get('edashed', False))
            if k.get('e'):
                mx, my = (cx + kx) / 2, (cy + h + ky) / 2
                txt = k['e']
                tw = len(txt.split('\n')[0]) * edge_fs * 0.62
                col = k.get('ec') or (edge_color if edge_color != '#1e1e1e' else ('#2f9e44' if '✓' in txt else '#e03131'))
                s.text(mx - tw - 16 if kx < cx else mx + 16, my - edge_fs * 1.1, txt, edge_fs, col, ff=nd.get('eff', 5))
        for k in ks:
            draw(k)

    draw(root)
    return pos
