import numpy as np
from typing import Sequence, Union, List
import math

# Define types for clarity
NumericSequence = Union[Sequence[float], np.ndarray, List[float]]

def python_rms(seq: NumericSequence) -> float:
    """
    Calculates the Root Mean Square (RMS) of a sequence using pure Python.
    Used for profiling comparison.
    """
    if not seq:
        return 0.0
    
    # Square each element and sum the results
    squared_sum = sum(x * x for x in seq)
    
    # Calculate the mean and take the square root
    return math.sqrt(squared_sum / len(seq))

def numpy_rms(arr: np.ndarray) -> float:
    """
    Calculates the Root Mean Square (RMS) of a NumPy array using fast vectorization.
    """
    if arr.size == 0:
        return 0.0
        
    # The vectorized way: np.mean of the squared array, then np.sqrt
    return np.sqrt(np.mean(arr**2))