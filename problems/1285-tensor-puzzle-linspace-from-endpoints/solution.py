import numpy as np

def linspace(start, stop, n: int) -> np.ndarray:
    """n evenly spaced values from start to stop inclusive."""
    # Your code here
    step = (stop - start) / max(n-1, 1)

    return start + step * np.arange(n, dtype=float)
