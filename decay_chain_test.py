import numpy as np

N_0 = float(input("Enter starting atom number: "))

N = np.array([N_0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
half_lives = np.array([4.44657e17, 1.797552e8, 2.196e4, 5.99184e7, 3.1104e5, 55, 0.14, 3.816e4, 3660, 3e-7, 186, np.inf])

decay_constants = np.zeros(len(half_lives))
decay_constants[:-1] = np.log(2) / half_lives[:-1]

p = 0.3995

transitions = {
    0: [(1, 1.0)],
    1: [(2, 1.0)],
    2: [(3, 1.0)],
    3: [(4, 1.0)],
    4: [(5, 1.0)],
    5: [(6, 1.0)],
    6: [(7, 1.0)],
    7: [(8, p), (10, 1 - p)],  # Element 8 branches
    8: [(9, 1.0)],             # Element 9 -> 10
    9: [(11, 1.0)],            # Element 10 -> stable
    10: [(11, 1.0)]             # Element 11 -> stable
}

def update_populations(N, decay_constants, transitions, dt):
    N_new = N.copy()

    for parent, daughters in transitions.items():
        # Number of atoms that decay during this time step
        probability_decay = 1 - np.exp(-decay_constants[parent] * dt)
        decayed = np.random.binomial(N[parent], probability_decay)

        N_new[parent] -= decayed

        # Distribute the decayed atoms among their possible daughters
        probabilities = [p for daughter, p in daughters]
        outcomes = np.random.multinomial(decayed, probabilities)

        for (daughter, p), number in zip(daughters, outcomes):
            N_new[daughter] += number

    return N_new

t = 0.0

with open("radioactive decay chain.txt", "w") as file:
    file.write(str(t) + " " + " ".join(map(str, N)) + "\n")

    while True:
        active_unstable = (N >= 1) & (decay_constants > 0)

        if not np.any(active_unstable):
            break

        shortest_half_life = (
            np.log(2) / np.max(decay_constants[active_unstable])
        )
        dt = 0.01 * shortest_half_life

        N = update_populations(N, decay_constants, transitions, dt)
        t += dt

        N[N < 1] = 0

        file.write(str(t) + " " + " ".join(map(str, N)) + "\n")