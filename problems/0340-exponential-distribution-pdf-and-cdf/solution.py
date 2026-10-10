import numpy as np
import math
def exponential_distribution(x: list, lam: float) -> dict:
    """
    Compute exponential distribution properties.
    
    Args:
        x: Points at which to evaluate PDF and CDF
        lam: Rate parameter (lambda) of the distribution
        
    Returns:
        Dictionary with 'pdf', 'cdf', 'mean', and 'variance' keys
    """
    exp_family = {'pdf': None, 'cdf': None, 'mean': None, 'variance': None}
    if lam <= 0:
        return exp_family
    
    else:
        exp_family['pdf'] = []
        exp_family['cdf'] = []
        exp_family['mean'] = round(1/lam, 4)
        exp_family['variance'] = round(1/(lam ** 2), 4)

    
    
    for samp in x:
        if samp < 0:
            exp_family['pdf'].append(0)
            exp_family['cdf'].append(0)

        else:
            exp_family['pdf'].append(round(lam * math.exp(-lam * samp), 4))
            exp_family['cdf'].append(round(1 - math.exp(-lam * samp), 4))

    return exp_family