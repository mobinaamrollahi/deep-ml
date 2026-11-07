import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	# the number of observations
	if not vectors:
		return []

	np_mat = np.array(vectors)
	cov = np.cov(np_mat)

	return cov.tolist()