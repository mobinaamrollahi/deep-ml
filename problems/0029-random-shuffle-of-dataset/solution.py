import numpy as np
import random

def shuffle_data(X, y, seed=None):
	np.random.seed(seed)
	idx = np.random.permutation(len(X))
	return X[idx], y[idx]