import numpy as np
from volforecast.simulate import simulate_const_vol
from volforecast.estimators import realized_variance

rng = np.random.default_rng(42)
sigma = 0.2 / np.sqrt(252)          # 20% annual volatility, in daily terms

log_prices = simulate_const_vol(sigma=sigma, n_days=200, n_steps=23400, rng=rng)
rv = realized_variance(log_prices, step=300)   # 5-minute returns

print("True variance:     ", sigma**2)
print("Average measured RV:", rv.mean())