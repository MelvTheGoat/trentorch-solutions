import numpy as np


def solve(x):
    """Implement Normalize a Vector from the mathematical contract in README.md."""
    v_norm = np.linalg.norm(x)
    if v_norm == 0:
        raise ValueError("Cannot normalize a zero vector")
    return x / v_norm
