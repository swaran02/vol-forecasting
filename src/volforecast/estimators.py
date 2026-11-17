import numpy as np

def realized_variance(log_prices: np.ndarray, step: int) -> np.ndarray:
    """
    Sum of squared returns per day, sampling every 'step' points. Returns shape (n_days).

    Sample the log prices using step
    The returns are the next minus the previous from the samples
    Square every return
    Add all the squared sampled returns to get the realized variance
    """

    sampled = log_prices[:, ::step]
    returns = np.diff(sampled, axis=1)
    squared = returns**2
    rv = np.sum(squared, axis=1)
    return rv

