import numpy as np


def solve(eigenvalues):
    """Implement Explained Variance Ratio from the mathematical contract in README.md."""
    eigenvalues = np.asarray(eigenvalues, dtype=float)
    total = np.sum(eigenvalues)
    if total == 0:
        return np.zeros_like(eigenvalues)
    return eigenvalues / total
