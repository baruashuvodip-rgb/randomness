import numpy as np

def decayed(N, decay_const, dt):
    
    return N*decay_const*dt

N_0 = float(input("Enter starting atom number: "))

N = np.array([N_0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
half_lives = np.array([4.44657e17, 1.797552e8, 2.196e4, 5.99184e7, 3.1104e5, 55, 0.14, 3.816e4, 3660, 3e-7, 186, np.inf])

decay_constants = np.zeros(len(half_lives))
decay_constants[:-1] = np.log(2) / half_lives[:-1]

t = 0.0

dt = np.zeros(len(half_lives))
dt[:-1] = 0.1 / decay_constants[:-1]

file = open("radioactive decay chain.txt","w")
iter = 0.0

while(N[11] < N_0):
    
    for i in range(0,len(N)-2):
        decay = decayed(N[i], decay_constants[i], dt[i])
        N[i] -= decay
        if i < 8:
            N[i+1] += decay

        elif i==8:
            N[9] += 0.6405*decay
            N[10] += 0.3595*decay

        else:
            N[11] +=decay
    
    iter += 1
    N = [int(x) for x in N]
    print(iter, N[0], N[11])
    file.write(f"{iter} ")
    file.write(" ".join(map(str, N)) + "\n")

file.close()

    
    
