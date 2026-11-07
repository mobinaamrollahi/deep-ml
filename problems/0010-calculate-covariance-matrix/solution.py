def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	# the number of observations
	if not vectors:
		return []

	N = len(vectors[0])
	f = len(vectors)
	averages = [sum(vectors[i]) / N for i in range(f)]
	cov = [[0.0] * f for _ in range(f)]

	for i in range(f):
		for j in range(i + 1):
			cov[i][j] = (1/(N-1)) * sum((vectors[i][k]-averages[i])*(vectors[j][k]-averages[j]) for k in range(N))
			cov[j][i] = cov[i][j]

	return cov