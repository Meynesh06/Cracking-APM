# Shared runner for the notes' code blocks (used by check_code.py and fixout.py).
# A block runs as its own process, from <project>/lab (so `from mylabhelpers import *` works), with the project's
# venv python if there is one (<project>/.venv), else the python running this script. Log noise is stripped from stderr.
# Results are cached per block text + a hash of every lab/*.py helper, so unchanged blocks are never re-run
# (NOCACHE=1 forces fresh runs). Runs are serialized by a lock file, so parallel writers do not fight over a small machine.
import glob, hashlib, json, os, re, subprocess, sys, tempfile
try:
    import fcntl
except ImportError:          # Windows: no lock, runs are still correct
    fcntl = None

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
LAB = os.path.join(ROOT, 'lab')
os.makedirs(LAB, exist_ok=True)
_CFG = {}
try:
    _CFG = json.load(open(os.path.join(ROOT, 'dkfile.json'))).get('lab', {}) or {}
except Exception:
    pass
_py = _CFG.get('python') or '.venv/bin/python'
PY = _py if os.path.isabs(_py) else os.path.join(ROOT, _py)
if not os.path.exists(PY):
    PY = sys.executable
TIMEOUT = int(_CFG.get('timeout', 600))
NOISE = re.compile(r'^(\d\d/\d\d/\d\d \d\d:\d\d:\d\d (WARN|INFO)\b.*|Using Spark.s default log4j.*|Setting default log level.*|'
                   r'To adjust logging level.*|Picked up JAVA_TOOL_OPTIONS.*|WARNING: .*|\s*)$')
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.codecache.json')
RCACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.runcache')
LOCK = os.path.join(tempfile.gettempdir(), 'dkfile-run-' + hashlib.sha1(ROOT.encode()).hexdigest()[:8] + '.lock')


def clean_err(err):
    return '\n'.join(l for l in err.split('\n') if not NOISE.match(l)).strip()


def run(code, timeout=None):
    """Run one block; return (stdout, cleaned stderr). Cached in tools/.runcache by block text + lab helper hash."""
    key = hashlib.sha1((_salt() + '\0' + code).encode()).hexdigest()
    f = os.path.join(RCACHE, key + '.json')
    if os.environ.get('NOCACHE') != '1' and os.path.exists(f):
        try:
            d = json.load(open(f))
            return d['out'], d['err']
        except Exception:
            pass
    out, err = _run(code, timeout or TIMEOUT)
    if not err.startswith('TIMEOUT'):
        os.makedirs(RCACHE, exist_ok=True)
        tmp = f + f'.{os.getpid()}'
        json.dump({'out': out, 'err': err}, open(tmp, 'w'))
        os.replace(tmp, f)
    return out, err


def _run(code, timeout):
    with tempfile.NamedTemporaryFile('w', suffix='.py', delete=False, dir=LAB, prefix='_blk_') as fh:
        fh.write(code)
        path = fh.name
    env = dict(os.environ, PYTHONPATH=LAB, PYTHONHASHSEED='0', PYSPARK_PYTHON=PY)
    lock = open(LOCK, 'w')
    try:
        if fcntl: fcntl.flock(lock, fcntl.LOCK_EX)
        p = subprocess.run([PY, path], capture_output=True, text=True, timeout=timeout, cwd=LAB, env=env)
        out, err = p.stdout, clean_err(p.stderr)
    except subprocess.TimeoutExpired:
        out, err = '', f'TIMEOUT after {timeout}s'
    finally:
        if fcntl: fcntl.flock(lock, fcntl.LOCK_UN)
        lock.close()
        os.unlink(path)
    return out, err


def _salt():
    h = hashlib.sha1(PY.encode())
    for f in sorted(glob.glob(os.path.join(LAB, '*.py'))):
        if not os.path.basename(f).startswith('_blk_'):
            h.update(open(f, 'rb').read())
    return h.hexdigest()[:12]


def cache_key(code, expected):
    return hashlib.sha1((_salt() + '\0' + code + '\0' + (expected or '')).encode()).hexdigest()


def cache_load():
    try:
        return json.load(open(CACHE))
    except Exception:
        return {}


def cache_save(c):
    tmp = CACHE + f'.{os.getpid()}'
    json.dump(c, open(tmp, 'w'))
    os.replace(tmp, CACHE)
