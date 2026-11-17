import numpy as np
rng = np.random.default_rng(42)
moves = rng.normal(0, 0.01, size=(2, 4))
print(moves)

a = np.array([[1, 2, 3],
              [4, 5, 6]])

a = np.cumsum(a, axis=1)

b = np.zeros((2,1))
c = np.hstack([b,a])
print(c)