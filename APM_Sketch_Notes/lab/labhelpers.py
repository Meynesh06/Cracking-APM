"""Lab helpers for APM Prep Sketch Notes: every run block starts with  from labhelpers import *

Rules that keep outputs identical on every run (the notes show real output, checked by tools/check_code.py):
  * no timestamps, durations, absolute paths, random ids or memory addresses in what you print
  * replace run-specific names with stable ones (see stable_names), sort before printing, seed every random generator
  * keep prints short (show(x, 5)); write files only under fresh("pN", "name")
"""
import os, random, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")          # inputs (made once by a gen_data.py you write; never written by blocks)
OUT = os.path.join(HERE, "out")            # everything blocks write
random.seed(0)


def path(*parts):
    """A path under lab/data."""
    return os.path.join(DATA, *parts)


def fresh(*parts):
    """An empty folder under lab/out (the old one is deleted), so a block can be re-run."""
    p = os.path.join(OUT, *parts)
    shutil.rmtree(p, ignore_errors=True)
    os.makedirs(p)
    return p


def stable_names(names, prefix="f", ext=""):
    """Map run-specific names (uuids, temp files) to f1, f2, ... in first-seen order."""
    m = {}
    for n in names:
        m.setdefault(n, f"{prefix}{len(m) + 1}{ext}")
    return m


def show(rows, n=10, cols=None):
    """Print a list of dicts / tuples, a pandas DataFrame or a pyarrow Table as a small aligned table, no index."""
    try:
        import pandas as pd
        if hasattr(rows, "to_pandas"):
            rows = rows.to_pandas()
        if isinstance(rows, pd.DataFrame):
            df = rows if cols is None else rows[cols]
            print(df.head(n).to_string(index=False))
            if len(df) > n:
                print(f"... ({len(df)} rows)")
            return
    except ImportError:
        pass
    rows = list(rows)
    for r in rows[:n]:
        print(r)
    if len(rows) > n:
        print(f"... ({len(rows)} rows)")


# Some native libraries (Rust / C++ worker threads) can abort the process during interpreter shutdown and print
# "terminate called without an active exception". Leave before that point, keeping the exit code of the script.
_FAILED = []


def _hard_exit():
    try:
        sys.stdout.flush(); sys.stderr.flush()
    finally:
        os._exit(1 if _FAILED else 0)


def _note_failure(hook):
    def wrapped(*a):
        _FAILED.append(1)
        hook(*a)
    return wrapped


sys.excepthook = _note_failure(sys.excepthook)
import atexit                              # noqa: E402
atexit.register(_hard_exit)
