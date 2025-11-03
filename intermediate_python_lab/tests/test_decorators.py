import logging, time
from ipylab.decorators import timed

def test_timed_decorator_threshold_logs_warning(caplog):
    caplog.set_level(logging.WARNING)
    @timed(threshold_ms=0.01)
    def sleepy():
        time.sleep(0.02)
        return 42
    out = sleepy()
    assert out == 42
    msgs = [r.message for r in caplog.records]
    assert any("SLOW CALL:" in m for m in msgs)
