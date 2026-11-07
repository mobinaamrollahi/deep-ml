import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	if not matrix:
		return []

	np_mat = np.array(matrix)
	
	if mode == 'column':
		means = np.mean(np_mat, axis=0)

	else:
		means = np.mean(np_mat, axis=1)
	return means.tolist()