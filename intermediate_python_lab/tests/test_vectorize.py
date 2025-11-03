import numpy as np
from ipylab.vectorize import python_rms, numpy_rms

def test_python_vs_numpy_rms_close():
    x = np.linspace(-1, 1, 1000)
    pr = python_rms(x.tolist())
    nr = numpy_rms(x)
    assert abs(pr - nr) < 1e-9
