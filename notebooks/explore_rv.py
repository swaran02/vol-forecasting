import numpy as np
from volforecast.simulate import simulate_const_vol
from volforecast.simulate import add_microstructure_noise
from volforecast.estimators import realized_variance

rng = np.random.default_rng(42)
sigma = 0.2 / np.sqrt(252)          # 20% annual volatility, in daily terms

log_prices = simulate_const_vol(sigma=sigma, n_days=200, n_steps=23400, rng=rng)
rv = realized_variance(log_prices, step=300)   # 5-minute returns

print("True variance:     ", sigma**2)
print("Average measured RV:", rv.mean())

print("Daily RV spread relative to truth:", rv.std() / sigma**2)

steps = [1, 5, 30, 60, 300, 900, 1800, 3900]

print(f"{'step':>6} {'n':>6} {'mean RV/true':>13} {'measured err':>13} {'predicted err':>14}")

for step in steps:
    rv = realized_variance(log_prices, step=step)
    n = 23400 // step
    mean_ratio = rv.mean() / sigma**2
    measured = rv.std() / sigma**2
    predicted = np.sqrt(2/n)
    print(f"{step:>6} {n:>6} {mean_ratio:>13.3f} {measured:>13.3f} {predicted:>14.3f}")

omega = 0.0001
noisy_prices = add_microstructure_noise(log_prices, omega=omega, rng=rng)

print(f"\n{'step':>6} {'n':>6} {'mean RV/true':>13} {'predicted':>10} {'total err':>10}")

for step in steps:
    rv = realized_variance(noisy_prices, step=step)          # measure from the noisy prices
    n = 23400 // step
    mean_ratio = rv.mean() / sigma**2                         # how biased is it?
    predicted = 1 + 2 * n * omega**2 / sigma**2               # what the bias formula says
    total_err = np.sqrt(np.mean((rv - sigma**2)**2)) / sigma**2   # bias and randomness combined
    print(f"{step:>6} {n:>6} {mean_ratio:>13.3f} {predicted:>10.3f} {total_err:>10.3f}")