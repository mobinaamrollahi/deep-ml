import torch

def make_tensor():
    """Return a 2x3 float32 tensor [[1, 2, 3], [4, 5, 6]]."""
    vector = [[1, 2, 3], [4, 5, 6]]
    return torch.tensor(vector, dtype=torch.float32)
