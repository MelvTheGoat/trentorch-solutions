import numpy as np


def solve(a, b):
    """Implement Cosine Similarity from the mathematical contract in README.md."""
    if np.all(a==0) or np.all(b==0):
        return 0.0
    dot = np.dot(a, b)
    magnitude_a = np.linalg.norm(a)
    magnitude_b = np.linalg.norm(b)
    magnitude = magnitude_a * magnitude_b
    cosine = float(dot / magnitude)
    return cosine
