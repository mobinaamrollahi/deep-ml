import numpy as np

def to_categorical(x, n_col=None):
	
	# take all the unique values of x
	x = np.asarray(x, dtype=int)

	if n_col is None:
		n_col = np.max(x) + 1

	encode = np.zeros((len(x), n_col))
	# sort them so that you can do the one hot encode
	encode[np.arange(len(x)), x] = 1.0

	return encode.tolist()