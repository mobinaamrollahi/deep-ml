import numpy as np
import math
def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
	"""
	Implements binary classification prediction using Logistic Regression.

	Args:
		X: Input feature matrix (shape: N x D)
		weights: Model weights (shape: D)
		bias: Model bias

	Returns:
		Binary predictions (0 or 1)
	"""
	pred = []
	for x in X:
		# x has a shape of (1 * D), weights has a shape of 1*D
		z = x @ weights.T + bias
		sigmoid = 1 / (1 + math.exp(-z))
		if sigmoid >= 0.5:
			pred.append(1)
		else:
			pred.append(0)
	
	return np.array(pred)