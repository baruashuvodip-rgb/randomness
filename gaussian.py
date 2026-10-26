import numpy as np

pi =3.14159265

def gaussian(x, std_dev, avg):
    
    return (1 / (std_dev * np.sqrt(2 * pi))) * np.exp(
        -0.5 * ((x - avg) / std_dev)**2)