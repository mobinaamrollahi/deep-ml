import numpy as np
import math

def log_softmax(scores: list) -> np.ndarray:
	logits = []
	den = sum([math.e**s for s in scores])
	for s in scores:
		logits.append(math.log(math.e**s/den))
	
	return np.array(logits)