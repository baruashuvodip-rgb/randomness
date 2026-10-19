import random
import numpy as np

x = random.random()
y = random.uniform(10,20) #uniform distribution i.e. all values have same probability
z = random.gauss(0,1000) #random numbers from gaussian distribution
i = random.randint(0,1000) #random, but integer values

n = np.random.random(10)

p = np.random.uniform(0,100,10)
q = np.random.randint(0,100,10)
r = np.random.normal(0,100,10) #same as gaussian
