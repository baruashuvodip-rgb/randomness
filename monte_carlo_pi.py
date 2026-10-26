import numpy as np

def monte_carlo_pi(N):
    x = np.random.uniform(0, 1, N)
    y = np.random.uniform(0, 1, N)
    r = np.sqrt(x*x + y*y)

    N_in = len(r[np.where(r <= 1)])
    pi_calculated = 4*N_in/N
    return pi_calculated