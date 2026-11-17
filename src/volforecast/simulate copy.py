import numpy as np

def simulate_constant_vol(sigma: float, n_steps:int, n_days:int, rng) -> np.ndarray:
    """Purpose: Create fake log-price paths that follow X = sigma * W"""


    """Log-price paths with constant volatility. Shape (n_days, n_steps + 1), each day starting at 0."""

    """
    Each day has T=1, so dt = 1/ n_steps

    Draw every increment once with rng.normal(0, sigma *np.sqrt(dt), size =(n_days, n_steps)) -> this is sigmadeltaW

    Cummulatively sum along each day with np.cumsum(..., axis=1), then put a column of zeros in front so each path starts at 0
    """

    ## Length of each interval is T/deltat

    dt = 1/n_steps

    ## Each move is sigma * deltaW ~ N with mean 0 and S.D sigma*root(dt)

    moves = rng.normal(0, sigma*np.sqrt(dt), size = (n_days, n_steps))

    ## Cummulatively sums moves along each day and then adds a column of zeros in front

    moves = np.cumsum(moves, axis=1)
    inzero = np.zeros((n_days,1))

    moves = np.hstack([inzero, moves])

    return moves

rng = np.random.default_rng(42)

print(simulate_constant_vol(0.02,4,2, rng=rng))





