import numpy as np

def simulate_const_vol(sigma : float, n_days : int, n_steps : int, rng) -> np.ndarray:
    """
    Purpose of this function is to create fake log price paths that follow X = sigma*W
    Length of each interval dt = T/n_steps, where T = 1 day
    Draw every increment with N(0, sigma*sqrt(dt)) with size = n_days, n_steps
    Finally cummulatively sum the moves for each day with move starting from 0

    """

    dt = 1/n_steps

    moves = rng.normal(0, sigma*np.sqrt(dt), size = (n_days, n_steps) )
    log_prices = np.cumsum(moves, axis=1)
    zer = np.zeros((n_days,1))
    log_prices = np.hstack([zer,log_prices])

    return log_prices




rng = np.random.default_rng(42)
print(simulate_const_vol(sigma=0.02, n_days=2, n_steps=4, rng=rng))