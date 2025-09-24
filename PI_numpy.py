import numpy as np

r = 1000
dot = 1_000_000
sim = 10

x = np.random.randint(1, r+1, size=(sim, dot))
y = np.random.randint(1, r+1, size=(sim, dot))

inn = np.sum(x*x + y*y <= r*r, axis=1)
pi_estimates = 4 * inn / dot

for i, val in enumerate(pi_estimates, 1):
    print(f"test{i} : {val}")

print("PI :", np.mean(pi_estimates))
