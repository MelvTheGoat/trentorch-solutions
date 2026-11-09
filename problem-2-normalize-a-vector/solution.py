import numpy as np


def solve(x):
    """Implement Normalize a Vector from the mathematical contract in README.md."""
    scale = np.asarray(np.abs(x), dtype=float)
    v_scaled = np.linalg.norm(x)
    if v_scaled == 0:
        raise ValueError("Cannot normalize a zero vector")
    return x / v_scaled
