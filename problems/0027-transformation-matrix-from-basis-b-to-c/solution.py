import numpy as np
def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	P = np.linalg.solve(np.array(C), np.array(B))
	return P.tolist()