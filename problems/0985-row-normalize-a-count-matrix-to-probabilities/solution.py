import numpy as np

def row_normalize(counts: list[list[float]]) -> list[list[float]]:
    """Convert a count matrix into a row-stochastic probability matrix."""
    # counts = np.asarray(counts, dtype=float)
    n = len(counts)
    for i in range(n):
        m = sum(counts[i])
        if m == 0:
            for j in range(len(counts[i])):
                counts[i][j] = 0 
        
        else:
            for j in range(len(counts[i])):
                counts[i][j] = counts[i][j] / m



    return counts