import time
import logging
from functools import wraps
from typing import Callable, Any

# Initialize a logger for the module
logger = logging.getLogger(__name__)

def timed(threshold_ms: float = None):
    """
    A decorator that times a function call and logs the result.

    Args:
        threshold_ms: If execution time exceeds this, a WARNING is logged (SLOW CALL).
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            start_time = time.perf_counter()
            
            # --- CRITICAL FIX: Capture the original function's result ---
            result = func(*args, **kwargs)
            
            end_time = time.perf_counter()
            elapsed_ms = (end_time - start_time) * 1000

            log_msg = f"'{func.__name__}' ran in {elapsed_ms:.2f} ms"

            if threshold_ms is not None and elapsed_ms > threshold_ms:
                # Log a WARNING for slow calls, as required by the test
                logger.warning(f"SLOW CALL: {log_msg}. Threshold: {threshold_ms:.2f} ms")
            else:
                logger.info(log_msg)

            # --- CRITICAL FIX: Return the captured result ---
            return result
        return wrapper
    return decorator