import numpy as np

def make_diagonal(x):
    x = np.asarray(x, dtype=float)

    return np.diag(x)