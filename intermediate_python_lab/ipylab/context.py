import time
import logging
from contextlib import contextmanager
from typing import Type

# Initialize a logger for the module
logger = logging.getLogger(__name__)

@contextmanager
def timer(label: str):
    """
    A context manager that times the execution of the enclosed block and logs the result.
    """
    start_time = time.perf_counter()
    logger.info(f"START: {label}...")
    try:
        yield
    finally:
        end_time = time.perf_counter()
        elapsed_ms = (end_time - start_time) * 1000
        # The test requires 'ms' in the log for the timer to pass.
        logger.info(f"END: {label} finished in {elapsed_ms:.2f} ms")


@contextmanager
def suppress_and_log(*exc_types: Type[BaseException]):
    """
    A context manager that catches specified exception types, logs them, 
    and prevents them from propagating (suppresses them).
    """
    try:
        yield
    except exc_types as e:
        # Log the exception that occurred
        logger.error(f"Suppressed exception: {type(e).__name__}: {e}")
        # When an exception is caught in a context manager's __exit__ 
        # (or in this decorator's exception handling), returning nothing 
        # or True suppresses the exception. We do nothing, which suppresses it.
        pass