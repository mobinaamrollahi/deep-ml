import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	min_ = data.min(axis=0)
	max_ = data.max(axis=0)
	mean_ = data.mean(axis=0)
	std_ = data.std(axis=0)
	normalized = (data - min_) / (max_ - min_)
	standardized = (data - mean_) / std_

	return standardized, normalized