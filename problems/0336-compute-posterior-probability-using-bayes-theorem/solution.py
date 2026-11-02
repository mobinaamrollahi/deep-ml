def bayes_theorem(priors: list[float], likelihoods: list[float]) -> list[float]:
	"""
	Calculate posterior probabilities using Bayes' Theorem.
	
	Args:
		priors: Prior probabilities P(H_i) for each hypothesis
		likelihoods: Likelihoods P(E|H_i) for each hypothesis
		
	Returns:
		Posterior probabilities P(H_i|E) for each hypothesis
	"""
	p = sum([priors[i] * likelihoods[i] for i in range(len(priors))])
	posts = [(priors[i] * likelihoods[i])/p for i in range(len(priors))]
	
	return posts