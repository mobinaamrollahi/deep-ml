import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    if norm_type == 'l1':
        arr = np.ravel(arr)
        return np.linalg.norm(arr, ord=1)

    elif norm_type == 'l2': 
        arr = np.ravel(arr)
        return np.linalg.norm(arr, ord=2)

    elif norm_type == 'linf':  
        arr = np.ravel(arr)
        return np.linalg.norm(arr, np.inf)

    else:
        if arr.ndim == 1:
            raise ValueError

        return np.linalg.norm(arr)
    

    
