# Build step-through traces for the "tracer" widgets.
# Usage: python3 make_traces.py notes.md [more.md ...]  ->  ../traces/<name>.json
#
# In the markdown:
#   <div class="tracer" data-trace="l4-print" data-code="print_1_to_n.py" data-call="print_n(3)" data-viz="none"></div>
# data-code names a ```python title="..."``` block (its function/class definitions are kept on
# their original lines, its top-level demo calls are blanked out) and data-call is what gets run.
# data-viz: none | list:NAME | stack:NAME | hanoi:N   (NAME is a variable created by data-call)
#           | grid:M[:i=var,j=var]   a 2-D list M with the current cell (i, j), the trail walked so far and the live rectangle
#           | range[:role=var,...]   a number line for search-on-answer: live [lo..hi], mid and the best answer so far (roles as below)
#           | window:NAME[:role=var,...]   a binary-search window over the list NAME: every step shows
#             the cells, the live [lo..hi] window, mid and the best candidate so far. The pointer variables
#             are found by their usual names (lo/low/start/left, hi/high/end/right, mid, res/ans/result...)
#             in the innermost traced frame that has them; role=var overrides (roles: lo, hi, mid, res).
import ast, io, json, os, re, sys, contextlib

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'traces')
os.makedirs(OUT, exist_ok=True)
FENCE = re.compile(r'^```python([^\n]*)\n(.*?)^```\s*$', re.S | re.M)
DIV = re.compile(r'<div class="tracer"((?:[^>"]|"[^"]*")*)></div>')   # a ">" inside a quoted attribute is fine
MAX_STEPS = 600


def attrs(s):
    return dict(re.findall(r'data-([\w-]+)="([^"]*)"', s))


def short(v, n=38):
    if v is None:
        return 'None'
    if callable(v) and not isinstance(v, type):            # a function / lambda argument: no memory address
        nm = getattr(v, '__name__', 'function')
        return 'λ' if nm == '<lambda>' else f'{nm}()'
    if hasattr(v, 'data') and hasattr(v, 'left'):          # a tree node
        return f'Node({v.data})'
    if isinstance(v, str):
        r = repr(v)
    else:
        r = repr(v)
    r = re.sub(r' at 0x[0-9a-fA-F]+', '', r)              # no memory addresses: traces must be the same on every run
    return r if len(r) <= n else r[:n - 1] + '…'


def defs_only(code):
    """Blank out top-level statements that are not definitions/imports, keeping line numbers."""
    tree = ast.parse(code)
    lines = code.split('\n')
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Import, ast.ImportFrom)):
            continue
        if isinstance(node, ast.Assign) and all(isinstance(t, ast.Name) and t.id.isupper() for t in node.targets):
            continue                                           # CONSTANTS stay
        for i in range(node.lineno - 1, node.end_lineno):
            lines[i] = ''
    return '\n'.join(lines)


def shown_code(code, call):
    """The widget shows the definitions and then the traced call in place of the demo lines."""
    tree = ast.parse(code)
    keep = (ast.FunctionDef, ast.ClassDef, ast.Import, ast.ImportFrom)
    drivers = [n for n in tree.body if not isinstance(n, keep)]
    if not drivers:
        return code
    first = min(n.lineno for n in drivers)
    if any(isinstance(n, keep) and n.lineno > first for n in tree.body):
        return code                      # demo lines in the middle: leave the code as it is
    head = code.split('\n')[:first - 1]
    while head and not head[-1].strip():
        head.pop()
    return '\n'.join(head + ['', call + '   # ▶ the call being traced'])


def hanoi_state(out, n):
    rods = {1: list(range(n, 0, -1)), 2: [], 3: []}
    for m in re.finditer(r'plate (\d+) from (\d) to (\d)', out):
        p, a, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if rods[a] and rods[a][-1] == p:
            rods[b].append(rods[a].pop())
    return [rods[1], rods[2], rods[3]]


def trace(code, call, viz):
    src = defs_only(code)
    lines = code.split('\n')
    g = {'__name__': '__trace__'}
    exec(compile(src, '<snippet>', 'exec'), g)
    steps, frames = [], []
    buf = io.StringIO()
    seen = [0]
    kind, _, vname = viz.partition(':')

    def look(name):
        for fr in reversed(frames):
            if name in fr.f_locals:
                return fr.f_locals[name]
        return g.get(name)

    ALIASES = {'lo': ('lo', 'low', 'start', 'left', 'l'), 'hi': ('hi', 'high', 'end', 'right', 'r'),
               'mid': ('mid', 'm'), 'res': ('res', 'ans', 'result', 'answer', 'first', 'last', 'best', 'cand')}
    NAMES = {}                              # role -> the variable name the code really uses (start / end / mid ...)
    arr_name, _, extra = vname.partition(':')
    roles = dict(kv.split('=') for kv in extra.split(',') if '=' in kv)

    def snap_window():
        arr = look(arr_name)
        a = [x if isinstance(x, (int, float, str)) or x is None else str(x) for x in (list(arr) if arr is not None else [])]
        p = {}
        for role, names in ALIASES.items():
            for nm in ([roles[role]] if role in roles else names):
                v = look(nm)
                if isinstance(v, int) and not isinstance(v, bool):
                    p[role] = v
                    NAMES.setdefault(role, nm)
                    break
        return {'a': a, 'p': p}

    def pointers(al=ALIASES, rl=roles):
        p = {}
        for role, names in al.items():
            for nm in ([rl[role]] if role in rl else names):
                v = look(nm)
                if isinstance(v, int) and not isinstance(v, bool):
                    p[role] = v
                    NAMES.setdefault(role, nm)
                    break
        return p

    GALIASES = {'i': ('i', 'row', 'r'), 'j': ('j', 'col', 'c')}

    def snap_grid():
        M = look(arr_name)
        mm = [[x if isinstance(x, (int, float, str)) or x is None else str(x) for x in row] for row in (M or [])]
        return {'m': mm, 'p': pointers(GALIASES, roles)}

    def snap_range():
        return {'p': pointers(ALIASES, roles)}

    def snap_viz():
        if kind == 'window':
            return snap_window()
        if kind == 'grid':
            return snap_grid()
        if kind == 'range':
            return snap_range()
        if kind in ('list', 'stack'):
            v = g.get(vname)
            return list(v) if v is not None else []
        if kind == 'hanoi':
            return hanoi_state(buf.getvalue(), int(vname))
        return None

    called = {}                          # frame id -> the arguments it was CALLED with

    def cur_args(fr):
        co = fr.f_code
        return [(a, short(fr.f_locals.get(a))) for a in co.co_varnames[:co.co_argcount]]

    def frame_label(fr):
        now = cur_args(fr)
        was = called.get(id(fr), now)
        lab = [fr.f_code.co_name, ', '.join(f'{a}={v}' for a, v in was)]
        changed = [f'{a}={v}' for (a, v), (_, w) in zip(now, was) if v != w]
        if changed:
            lab.append(', '.join(changed))   # a parameter was re-assigned inside the call
        return lab

    def record(ev, fr, extra=None):
        text = buf.getvalue()
        d = text[seen[0]:]
        seen[0] = len(text)
        ln = fr.f_lineno
        st = {'ln': ln, 'ev': ev, 'st': [frame_label(f) for f in frames]}
        if d:
            st['d'] = d
        v = snap_viz()
        if v is not None:
            st['v'] = v
        if ev == 'call':
            name, args = frame_label(fr)[:2]
            depth = len(frames)
            st['say'] = f'call {name}({args})' + (' · the first call' if depth == 1 else f' · frame #{depth} goes on the stack')
        elif ev == 'line':
            src_line = lines[ln - 1].split('#')[0].strip()
            st['say'] = src_line
            m = re.match(r'(?:el)?if (.+):$', src_line)
            if m and not re.search(r'\b(?!len\b|abs\b|max\b|min\b)\w+\(', m.group(1)):
                try:
                    val = eval(m.group(1), fr.f_globals, dict(fr.f_locals))
                    st['say'] += f'   → {bool(val)}'
                except Exception:
                    pass
        elif ev == 'return':
            name, args = frame_label(fr)[:2]
            r = extra
            if len(frames) > 1:
                cn, ca = frame_label(frames[-2])[:2]
                tail = f' · frame pops, back in {cn}({ca})'
            else:
                tail = ' · the whole call is finished'
            st['say'] = f'{name}({args}) is done' + (f' → returns {short(r)}' if r is not None else '') + tail
        steps.append(st)
        if len(steps) > MAX_STEPS:
            raise RuntimeError('trace too long: ' + call)

    def tracer(fr, ev, arg):
        if fr.f_code.co_filename != '<snippet>':
            return None
        if fr.f_code.co_name in ('<listcomp>', '<genexpr>', '<dictcomp>', '<setcomp>'):
            return None                  # comprehensions are one step of their line (Python 3.12+ inlines them anyway)
        if ev == 'call':
            frames.append(fr)
            called[id(fr)] = cur_args(fr)
            record('call', fr)
        elif ev == 'line':
            record('line', fr)
        elif ev == 'return':
            record('return', fr, arg)
            frames.pop()
        return tracer

    # setup statements (e.g. "s = [5, 4, 3]") run untraced, the last statement is traced
    parts = [p.strip() for p in call.split(';') if p.strip()]
    with contextlib.redirect_stdout(buf):
        for p in parts[:-1]:
            exec(p, g)
        seen[0] = len(buf.getvalue())
        start_viz = snap_viz()
        sys.settrace(tracer)
        try:
            exec(parts[-1], g)
        finally:
            sys.settrace(None)
    # final state after the last return
    tail = buf.getvalue()[seen[0]:]
    if tail:
        steps[-1]['d'] = steps[-1].get('d', '') + tail
    res = {'call': parts[-1], 'setup': '; '.join(parts[:-1]), 'viz': kind or 'none', 'steps': steps}
    if start_viz is not None:
        res['v0'] = start_viz
    if kind == 'hanoi':
        res['n'] = int(vname)
    if kind in ('window', 'grid', 'range'):
        res['names'] = NAMES
    return res


def main(paths):
    made = 0
    for md in paths:
        text = open(md).read()
        blocks = {}
        for m in FENCE.finditer(text):
            t = re.search(r'title="([^"]+)"', m.group(1))
            if t:
                blocks.setdefault(t.group(1), m.group(2))
        for m in DIV.finditer(text):
            a = attrs(m.group(1))
            code = blocks.get(a['code'])
            if code is None:
                raise SystemExit(f'{md}: no python block titled {a["code"]} for trace {a["trace"]}')
            code = code.rstrip('\n')
            res = trace(code, a['call'], a.get('viz', 'none'))
            res['code'] = shown_code(code, res['call'])
            res['title'] = a['code']
            with open(os.path.join(OUT, a['trace'] + '.json'), 'w') as f:
                json.dump(res, f, separators=(',', ':'))
            made += 1
            print(f"trace {a['trace']:<22} {len(res['steps']):>4} steps  ({a['call']})")
    print('traces written:', made)


if __name__ == '__main__':
    main(sys.argv[1:])
