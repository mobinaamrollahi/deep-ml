import numpy as np

def gaussian_mle(data: np.ndarray) -> tuple:
    mean_ = data.mean()
    std_sum = 0
    for i in range((len(data))):
        std_sum += (data[i] - mean_) ** 2

    std_gu = (std_sum) / (len(data))
    # Your code here
    return mean_, std_gu