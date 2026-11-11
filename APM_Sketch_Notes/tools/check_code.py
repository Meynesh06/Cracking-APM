# Runs every ```python block that is followed by an ```output / ```error block
# and compares the real result. Blocks marked "nocheck" are skipped.
# Usage: python3 check_code.py notes/parts/l2.md [more.md ...]
import re, subprocess, sys, tempfile, os
import runner as spark_run
CACHE = spark_run.cache_load()
NOCACHE = os.environ.get('NOCACHE') == '1'

FENCE = re.compile(r'^```(\w+)([^\n]*)\n(.*?)^```\s*$', re.S | re.M)

def run(code, cwd=None):
    with tempfile.NamedTemporaryFile('w', suffix='.py', delete=False, dir=cwd) as f:
        f.write(code)
        path = f.name
    try:
        p = subprocess.run([sys.executable, path], capture_output=True, text=True, timeout=20, cwd=cwd)
    finally:
        os.unlink(path)
    return p.stdout, p.stderr

# A part can opt into "session" mode with <!-- check: session -->: every python block then runs,
# in order, inside one shared temp folder (so files written by one block exist for the next),
# and ```file title="name"``` blocks are compared with the real file contents at that point.
# <!-- check: fixture NAME --> creates a small binary (JPEG-like) file before the run.
# <!-- check: module NAME.py --> ```python title="NAME.py"``` blocks are written to disk as modules.

total = bad = skipped = 0
norm = lambda t: '\n'.join(l.rstrip() for l in t.rstrip('\n').split('\n'))  # ignore trailing spaces
def session(md, text, blocks):
    global total, bad, skipped
    d = tempfile.mkdtemp(prefix='chk_')
    for fx in re.findall(r'<!-- check: fixture ([\w.-]+) -->', text):
        with open(os.path.join(d, fx), 'wb') as f:
            f.write(bytes([0xFF, 0xD8, 0xFF, 0xE0, 0x00, 0x10]) + b'JFIF\x00' + bytes(range(256)) * 4 + bytes([0xFF, 0xD9]))
    modules = set(re.findall(r'<!-- check: module ([\w./-]+) -->', text))
    for i, (lang, info, body, pos) in enumerate(blocks):
        line = text[:pos].count('\n') + 1
        title = (re.search(r'title="([^"]+)"', info) or [None, None])[1]
        if lang == 'file':
            total += 1
            got = open(os.path.join(d, title)).read() if os.path.exists(os.path.join(d, title)) else '<missing>'
            if got.rstrip('\n') != body.rstrip('\n'):
                bad += 1
                print(f'--- {md}:{line} FILE MISMATCH {title}\nexpected:\n{body}\ngot:\n{got}')
            continue
        if lang != 'python':
            continue
        if title in modules:
            os.makedirs(os.path.dirname(os.path.join(d, title)) or d, exist_ok=True)
            open(os.path.join(d, title), 'w').write(body)
            continue
        following = []
        j = i + 1
        while j < len(blocks) and blocks[j][0] in ('output', 'error'):
            following.append(blocks[j]); j += 1
        if 'nocheck' in info or any('nocheck' in f[1] for f in following):
            skipped += 1
            continue
        out, err = run(body, cwd=d)
        if not following:
            if err.strip():
                bad += 1
                print(f'--- {md}:{line} UNEXPECTED STDERR (no expected block)\n{err[-400:]}')
            continue
        total += 1
        check(md, line, following, out, err)

def check(md, line, following, out, err):
    global bad
    exp_out = next((f[2] for f in following if f[0] == 'output'), None)
    exp_err = next((f[2] for f in following if f[0] == 'error'), None)
    ok = True
    if exp_out is not None and norm(out) != norm(exp_out):
        ok = False
        print(f'--- {md}:{line} OUTPUT MISMATCH\nexpected:\n{exp_out}\ngot:\n{out}\nstderr:\n{err[-400:]}')
    if exp_err is not None:
        last = err.strip().splitlines()[-1] if err.strip() else ''
        if last != exp_err.strip().splitlines()[-1]:
            ok = False
            print(f'--- {md}:{line} ERROR MISMATCH\nexpected: {exp_err.strip()}\ngot: {last}')
    elif err.strip():
        ok = False
        print(f'--- {md}:{line} UNEXPECTED STDERR\n{err[-400:]}')
    if not ok:
        bad += 1

def run_cpp(code):
    d = tempfile.mkdtemp(prefix='cpp_')
    src, exe = os.path.join(d, 'main.cpp'), os.path.join(d, 'main')
    open(src, 'w').write(code)
    c = subprocess.run(['g++', '-std=c++17', '-O1', '-w', src, '-o', exe], capture_output=True, text=True)
    if c.returncode:
        return '', 'COMPILE ERROR\n' + c.stderr
    p = subprocess.run([exe], capture_output=True, text=True, timeout=20)
    return p.stdout, p.stderr

cpp_total = 0
clean = 0
for md in sys.argv[1:]:
    text = open(md).read()
    blocks = [(m.group(1), m.group(2), m.group(3), m.start()) for m in FENCE.finditer(text)]
    if '<!-- check: session -->' in text:
        session(md, text, blocks)
        continue
    for i, (lang, info, body, pos) in enumerate(blocks):
        if lang not in ('python', 'cpp'):
            continue
        if 'nocheck' in info:
            skipped += 1
            continue
        following = []
        j = i + 1
        while j < len(blocks) and blocks[j][0] in ('output', 'error'):
            # only if they come right after (no other python block in between)
            following.append(blocks[j])
            j += 1
        line = text[:pos].count('\n') + 1
        if not following:
            # no expected output: it must at least run cleanly (fragments are marked nocheck)
            key = spark_run.cache_key(body, '')
            if not NOCACHE and CACHE.get(key) == 'ok':
                clean += 1
                continue
            out, err = run_cpp(body) if lang == 'cpp' else spark_run.run(body)
            if not err.strip():
                CACHE[key] = 'ok'; spark_run.cache_save(CACHE)
            if err.strip():
                bad += 1
                print(f'--- {md}:{line} FAILS TO RUN (no expected block)\n{err[-500:]}')
            else:
                clean += 1
            continue
        if any('nocheck' in f[1] for f in following):
            skipped += 1
            continue
        total += 1
        exp_out = next((f[2] for f in following if f[0] == 'output'), None)
        exp_err = next((f[2] for f in following if f[0] == 'error'), None)
        key = spark_run.cache_key(body, (exp_out or '') + '\0' + (exp_err or ''))
        if not NOCACHE and CACHE.get(key) == 'ok':
            continue
        if lang == 'cpp':
            cpp_total += 1
            out, err = run_cpp(body)
        else:
            out, err = spark_run.run(body)
        ok = True
        if exp_out is not None and norm(out) != norm(exp_out):
            ok = False
            print(f'--- {md}:{line} OUTPUT MISMATCH\nexpected:\n{exp_out}\ngot:\n{out}\nstderr:\n{err[-400:]}')
        if exp_err is not None:
            last = err.strip().splitlines()[-1] if err.strip() else ''
            if last != exp_err.strip().splitlines()[-1]:
                ok = False
                print(f'--- {md}:{line} ERROR MISMATCH\nexpected: {exp_err.strip()}\ngot: {last}')
        elif err.strip():
            ok = False
            print(f'--- {md}:{line} UNEXPECTED STDERR\n{err[-400:]}')
        if not ok:
            bad += 1
        else:
            CACHE[key] = 'ok'
            spark_run.cache_save(CACHE)
print(f'checked {total} blocks against their output ({cpp_total} C++), {clean} more ran cleanly, {bad} problems, {skipped} skipped (nocheck)')
