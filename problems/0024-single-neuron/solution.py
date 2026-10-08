import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	probabilities = []
	for f in features:
		# dim of f is (1, D), 
		pred_r = sum([f[i] * weights[i] for i in range(len(f))]) + bias
		pred = 1 / (1 + math.exp(-pred_r))
		probabilities.append(pred)

	mse = sum([(labels[i] - probabilities[i])**2 for i in range(len(labels))]) / len(labels)
	return probabilities, mse