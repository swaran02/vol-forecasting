"""
rng = np.random.default_rng(42)
sigma = 0.2 / np.sqrt(252)
paths = simulate_constant_vol(sigma, n_steps=23400, n_days=200, rng=rng)
rv = realized_variance(paths, step=300)   # 300 seconds = 5 minutes
print(rv.mean(), sigma**2)
"""