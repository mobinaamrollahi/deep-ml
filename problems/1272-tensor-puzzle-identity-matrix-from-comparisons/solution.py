import numpy as np

def eye(n: int) -> np.ndarray:
    """n x n identity matrix without np.eye."""
    mat = [[0.] * n for _ in range(n)] 
    for i in range(n):
        mat[i][i] = 1

    return np.asarray(mat, dtype=float)
