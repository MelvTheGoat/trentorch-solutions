import numpy as np


def solve(x):
    """Implement Logistic Sigmoid from the mathematical contract in README.md."""
    result = []
    for c in x:
        if c  < 0:
            c = np.exp(c) / (1 + np.exp(c))
            result.append(c)
        else:
            c = 1 / (1 + np.exp(-c))
            result.append(c)
    return np.array(result, dtype=float)
