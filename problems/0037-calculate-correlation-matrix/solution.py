import numpy as np

def calculate_correlation_matrix(X, Y=None):
    X = np.asarray(X, dtype=float)
    Y = X if Y is None else np.asarray(Y, dtype=float)
    n = X.shape[1]
    return np.corrcoef(X, Y, rowvar=False)[:n, n:]
