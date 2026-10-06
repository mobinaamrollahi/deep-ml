from typing import Callable
import numpy as np

def newtons_method_optimization(
	gradient_func: Callable[[list[float]], list[float]],
	hessian_func: Callable[[list[float]], list[list[float]]],
	x0: list[float],
	tol: float = 1e-6,
	max_iter: int = 100
) -> list[float]:
	"""
	Find the minimum of a function using Newton's method.
	
	Args:
		gradient_func: Function that returns gradient vector at a point
		hessian_func: Function that returns Hessian matrix at a point
		x0: Initial guess (list of coordinates)
		tol: Convergence tolerance for gradient norm
		max_iter: Maximum number of iterations
		
	Returns:
		The point that minimizes the function
	"""
	point = np.array(x0, dtype=float)
	for _ in range(max_iter):
		grad = gradient_func(point)
		hess = hessian_func(point)
		delta = np.linalg.solve(np.array(hess), np.array(grad))
		point -= delta
		if np.linalg.norm(grad) < tol:
			break
	return point.tolist()
