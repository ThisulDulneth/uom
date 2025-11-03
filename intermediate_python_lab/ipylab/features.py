import numpy as np
from typing import List, Union

# Note: The input x must be a NumPy array for this file to work efficiently
Array = np.ndarray

def feature_vector(x: Array) -> List[Union[float, int]]:
    """
    Calculates key statistical features for a 1-D signal array.

    Features returned in order:
    1. RMS (Root Mean Square)
    2. Zero Crossings (Count)
    3. Peak-to-Peak (Max - Min)
    4. MAD (Median Absolute Deviation)
    """
    if x.size == 0:
        return [0.0, 0, 0.0, 0.0]

    # 1. RMS (Root Mean Square)
    rms = np.sqrt(np.mean(x**2))
    
    # 2. Zero Crossings (Count)
    # np.sign(x) returns -1, 0, or 1. diff() calculates the difference between adjacent signs.
    # The result is non-zero only when the sign changes (crossing zero).
    # We divide by 2 because the change is always -2 or 2 for a full crossing.
    zero_crossings = int(np.sum(np.abs(np.diff(np.sign(x))))) // 2
    
    # 3. Peak-to-Peak
    peak_to_peak = np.max(x) - np.min(x)
    
    # 4. MAD (Median Absolute Deviation)
    # The median absolute deviation of the data (median(|x - median(x)|))
    mad = np.median(np.abs(x - np.median(x)))
    
    return [rms, zero_crossings, peak_to_peak, mad]