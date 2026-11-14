import numpy as np

def make_diagonal(x):
    x = np.asarray(x, dtype=float)
    n = x.shape[0]
    diag_mat = [[0.]* n for _ in range(len(x))] 
    for i in range(n):
        diag_mat[i][i] = x[i]

    return diag_mat