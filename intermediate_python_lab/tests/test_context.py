import logging, re
from ipylab.context import timer, suppress_and_log

def test_timer_runs_and_logs(caplog):
    caplog.set_level(logging.INFO)
    with timer("unit-test"):
        x = sum(range(1000))
    msgs = [r.message for r in caplog.records]
    assert any("unit-test" in m and "ms" in m for m in msgs)

def test_suppress_and_log(caplog):
    caplog.set_level(logging.ERROR)
    with suppress_and_log(ValueError):
        int("not-int")  # should not raise
    # Should have logged an exception
    msgs = [r.message for r in caplog.records]
    assert any("invalid literal" in m for m in msgs)
