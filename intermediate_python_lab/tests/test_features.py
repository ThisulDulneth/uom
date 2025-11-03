import numpy as np
from ipylab.features import feature_vector

def test_feature_vector_simple():
    x = np.array([0.0, 1.0, -1.0, 1.0, -1.0])
    rms, zc, p2p, mad = feature_vector(x)
    assert round(rms, 4) == round(( (0**2+1+1+1+1)/5 )**0.5, 4)
    assert zc >= 3  # has several zero crossings
    assert p2p == 2.0
    assert mad > 0
