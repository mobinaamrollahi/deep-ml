import numpy as np
import math

def gibbs_softmax_action_selection(q_values: list, temperature: float, seed: int) -> tuple:
    """
    Perform Gibbs softmax (Boltzmann) action selection.

    Args:
        q_values: list of floats, estimated action values
        temperature: float, temperature parameter (tau > 0)
        seed: int, random seed for reproducibility

    Returns:
        tuple: (probabilities as list of floats, selected action as int)
    """
    np.random.seed(seed)
    probs = []
    den = sum([math.e**(q/temperature) for q in q_values])
    for q in q_values:
        probs.append(math.e**(q/temperature)/den)
    
    return probs, np.random.choice(range(len(probs)), p=probs)