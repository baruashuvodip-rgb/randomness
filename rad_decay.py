import math

N = float(input("Enter number of starting atoms: "))
decay_const = float(input("Enter decay constant: "))

if N < 0 or decay_const <= 0:
    raise ValueError("N must be nonnegative and decay constant must be positive.")

exponent = -1*math.floor(math.log10(decay_const))
dt = pow(10, exponent-1)

def decayed(N, decay_const):
    
    return N*decay_const*dt

file = open("radioactive decay.txt","w")
t = 0.0
while(N>0):

    N -=decayed(N, decay_const)
    t += dt
    if N<1:
        N = 0
        
    file.write(f"{t} {N}\n")

file.close()

#the plot of N vs t is an exponential decay curve.



