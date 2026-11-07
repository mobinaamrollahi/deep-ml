import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method

	if len(a) * len(a[0]) != new_shape[0] * new_shape[1]:
		return []

	r, c = len(a), len(a[0])
	n_r, n_c = new_shape[0], new_shape[1]
	reshaped_matrix = [[0.0] * n_c for _ in range(n_r)] 
	k, w = 0, 0
	for i in range(n_r):
		for j in range(n_c):
			if w == c:
				k += 1
				w = 0

			reshaped_matrix[i][j] = a[k][w]
			w += 1
	return reshaped_matrix