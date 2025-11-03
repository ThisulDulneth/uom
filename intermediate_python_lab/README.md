# Intermediate Python Lab — *Signal Log Analyzer*
A hands-on lab to practice **generators, context managers, decorators, dataclasses, pathlib, itertools, functools (caching/partial), and NumPy vectorization**.

## Story
You have a CSV of 1‑D sensor readings (a noisy mixture of sine and square waves). Build a small toolkit that:
- Streams data in chunks (generators)
- Applies moving statistics (average & median)
- Extracts vectorized features (NumPy)
- Uses context managers for timing and controlled exception handling
- Adds a timing decorator with a slow-call warning
- Wraps configuration in a frozen dataclass
- Reads/writes files via `pathlib`
- (Optional) exposes a tiny CLI via `typer`

## What you’ll build
```
intermediate_python_lab/
  data/
    signal.csv                  # synthetic dataset (already generated)
  src/ipylab/
    __init__.py
    config.py                   # dataclass config (TODOs inside)
    context.py                  # timer & suppress_and_log (TODOs)
    decorators.py               # @timed decorator (TODOs)
    generators.py               # chunks, moving_average, moving_median (TODOs)
    features.py                 # vectorized features (TODOs)
    io.py                       # load/save with pathlib (TODOs)
    vectorize.py                # RMS: python vs numpy (TODOs)
    cli.py                      # optional: typer commands (TODOs)
  tests/
    test_context.py
    test_decorators.py
    test_generators.py
    test_features.py
    test_vectorize.py
  README.md
  requirements.txt
```

## Setup
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
```

## Tasks (Checkpointed)
1) **Dataclass config:** Complete `LabConfig` (frozen, sensible defaults) in `config.py`.
2) **Context managers:** Implement `timer(label)` and `suppress_and_log(*exc_types)` in `context.py`.
3) **Decorator:** Implement `@timed(threshold_ms=None)` in `decorators.py` (uses wraps; logs WARNING if slow).
4) **Generators:** 
   - `chunks(iterable, size)` as an iterator
   - `moving_average(window)` **generator** (stateful; accepts values via `.send(x)`)
   - `moving_median(window)` **generator**
5) **Vectorization:** Implement `python_rms(seq)` and `numpy_rms(arr)` in `vectorize.py`.
6) **Features:** In `features.py`, implement `feature_vector(x)` returning `[rms, zero_crossings, peak_to_peak, mad]` using NumPy.
7) **I/O:** In `io.py`, implement `load_signal_csv(path)` and `save_features_csv(path, rows)` with `pathlib.Path`; handle errors.
8) **CLI (optional):** In `cli.py`, wire `generate-data`, `run-pipeline`, `profile` commands with `typer`.

Run `pytest -q` frequently. Start with `generators` and `vectorize`—they’re the foundation.

## Stretch
- Add `functools.lru_cache` to memoize an intentionally expensive function.
- Add `itertools` utilities (`pairwise`, `accumulate`) to compute diffs/rolling sums.
- Use `@dataclass(slots=True)` and compare attribute access speed.

## Grading rubric (suggested)
- Correctness (tests pass): 60%
- Code clarity & types/docstrings: 20%
- Robustness (error handling, logging): 10%
- Optional CLI / stretch: 10%

Happy hacking!
