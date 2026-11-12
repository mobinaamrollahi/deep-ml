import numpy as np

def calculate_latency_percentiles(latencies: list[float]) -> dict[str, float]:
    """
    Calculate P50, P95, and P99 latency percentiles.
    
    Args:
        latencies: List of latency measurements
    
    Returns:
        Dictionary with keys 'P50', 'P95', 'P99' containing
        the respective percentile values rounded to 4 decimal places
    """
    if not latencies:
        return {'P50': 0.0, 'P95': 0.0, 'P99': 0.0}
    np_late = np.array(latencies)
    percentiles = {'P50': np.round(np.percentile(np_late, 50), 4).tolist(), 'P95': np.round(np.percentile(np_late, 95), 4).tolist(), 'P99': np.round(np.percentile(np_late, 99), 4).tolist()}

    return percentiles