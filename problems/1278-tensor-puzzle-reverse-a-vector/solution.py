import numpy as np

def flip(a: np.ndarray) -> np.ndarray:
    """Reverse 1-D array a without slicing a[::-1]."""
    # Your code here
    n = a.shape[0]
    i = np.arange(n)
    idx = n - 1 - i
    
    return a[idx]
