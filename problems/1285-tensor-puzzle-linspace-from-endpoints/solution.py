import numpy as np

def linspace(start, stop, n: int) -> np.ndarray:
    """n evenly spaced values from start to stop inclusive."""
    # Your code here
    if n == 1:
        return np.asarray([start], dtype = float)
        
    else:
        sol = np.zeros(n)

    for i in range(n):
        sol[i] = start + ((stop - start) / (n-1)) * i

    return sol
