def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
    import numpy as np
    """
    Compute the determinant and trace of a square matrix.
    
    Args:
        matrix: A square matrix (n x n) represented as list of lists
    
    Returns:
        Tuple of (determinant, trace)
    """
    matrix = np.asarray(matrix, dtype=float)
    det_matrix = np.linalg.det(matrix)
    
    return np.linalg.det(matrix), np.trace(matrix)