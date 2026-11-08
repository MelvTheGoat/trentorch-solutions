import numpy as np


def solve(x):
    """Implement Compute a Stable L2 Norm from the mathematical contract in README.md."""
    x = np.asarray(x, float)
    xm = np.max(np.abs(x))
    if all(x) > 0: 
        norm = xm * np.sqrt(np.sum((x/xm)**2))
    return norm
