def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    import numpy as np 
    np_matrix = np.array(matrix)
    return (np_matrix * scalar).tolist()