import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	batches = []
	n = len(X)
	X = X.tolist()
	if y is not None:
		y = y.tolist()
		for i in range(0, n, batch_size):
			batches.append([X[i:i+batch_size], y[i:i+batch_size]])
	else:
		for i in range(0, n, batch_size):
			batches.append([X[i:i+batch_size]])


	return batches