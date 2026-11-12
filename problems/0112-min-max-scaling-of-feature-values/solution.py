def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    import numpy as np
    np_x = np.array(x)
    max_x = np_x.max()
    min_x = np_x.min()
    norm_x = [(term - min_x)/(max_x - min_x) for term in np_x]
    return norm_x