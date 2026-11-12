# Explained Variance Ratio

Intermediate | problemset | unsupervised-ml | pca

Convert the eigenvalues of a covariance matrix into explained-variance ratios: each eigenvalue divided by their sum.

Implement `solve(eigenvalues)`.

**Returns.** Return a NumPy vector that sums to 1. If the eigenvalues sum to zero, return a vector of zeros.

### Examples

**Example 1**

Input:

```python
solve([2.0, 1.0])
```

Output:

```text
[0.666667, 0.333333]
```

**Example 2**

Input:

```python
solve([5.0, 3.0, 2.0])
```

Output:

```text
[0.5, 0.3, 0.2]
```

**Example 3**

Input:

```python
solve([0.0, 0.0])
```

Output:

```text
[0.0, 0.0]
```
