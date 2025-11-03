import statistics
from typing import Iterable, List, Generator, Any, TypeVar

T = TypeVar('T')

def chunks(iterable: Iterable[T], size: int) -> Generator[List[T], None, None]:
    """
    Generates successive n-sized chunks from an iterable.
    """
    # 1. Convert to an iterator for efficient pulling of data
    iterator = iter(iterable)
    while True:
        chunk = []
        for _ in range(size):
            try:
                # 2. Append the next item from the iterator
                chunk.append(next(iterator))
            except StopIteration:
                # 3. If iteration stops, yield any remaining partial chunk and exit
                if chunk:
                    yield chunk
                return
        # 4. Yield the full chunk of size 'size'
        yield chunk

def moving_average(window: int) -> Generator[float, float, None]:
    """
    A stateful generator (coroutine) for calculating a moving average.
    Accepts values via .send(x).
    """
    history: List[float] = []
    # Use while True to allow continuous sending and prevent StopIteration error
    while True:
        # 'yield' is used to return a value (the current average)
        # The result of 'yield' is the value sent via .send()
        current_avg = statistics.mean(history) if history else None
        new_value = yield current_avg

        if new_value is not None:
            history.append(new_value)
            # Maintain the window size
            if len(history) > window:
                history.pop(0)

def moving_median(window: int) -> Generator[float, float, None]:
    """
    A stateful generator (coroutine) for calculating a moving median.
    Accepts values via .send(x).
    """
    history: List[float] = []
    # Use while True to allow continuous sending and prevent StopIteration error
    while True:
        # 'yield' returns the current median
        current_med = statistics.median(history) if history else None
        new_value = yield current_med

        if new_value is not None:
            history.append(new_value)
            # Maintain the window size
            if len(history) > window:
                history.pop(0)