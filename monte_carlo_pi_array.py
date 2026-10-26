import numpy as np
import monte_carlo_pi as mcp
import gaussian

N_iteration = int(input("How many values of Pi do you want to generate? "))
N = int(input("How many points do you want to use for each value? "))

pi_values = []

for i in range(0,N_iteration):
    
    pi_values.append(mcp.monte_carlo_pi(N))

average_pi = np.average(pi_values)
std_dev_pi = np.std(pi_values)

print("The average value of Pi has been calculated to be", average_pi, "with a standard deviation of", std_dev_pi)

import matplotlib.pyplot as plt
plt.hist(pi_values, bins='fd', density=True, label="Pi")
plt.xlabel("Value of Pi")
plt.ylabel("Number of instances")


points = np.linspace(np.min(pi_values), np.max(pi_values), 1000)

gauss = [gaussian.gaussian(point, np.std(pi_values), np.average(pi_values)) for point in points]

plt.plot(points, gauss, label="Gaussian")
plt.xlabel("Value of Pi")
plt.ylabel("Gaussian Probability")

plt.show()

#the histogram bars follow the gaussian distribution quite closely. at first this my seem odd since
#we used a uniform distribution, but the uniform distribution was for the points all over the square. 
#it doesn't mean that our calculated pi values will also follow a uniform distribution.
#rather the pi values should be distributed around the actual value of pi, which matches the gaussian curve.

#when evaluating with N_iteration=100000, N=10000, the average value and standard deviation remain almost identical,
#but the histogram shows spikes distributed almost evenly across the values, with the spikes themselves following 
#a Gaussian-like distribution.
#i think this has to do with the nature of the histogram and the bin sizes. with 10 times as many values of pi as before but with no increase in 
#accuracy, there are bound to be some clusters where there are significantly more instances of some values than others. 
#i am not sure why the spikes themselves seem to follow a gaussian distribution, however.

#the spikes do not vanish when N is increased to 100000, though they do not stand out as much as they did before, 
# i.e. the values conform more closely to the Gaussian distribution.
# this seems to support my earlier hypothesis insofar as increasing accuracy causes the histogram to become smoother.
#notably, the standard deviation has decreased significantly, from 0.0165 to 0.0052.