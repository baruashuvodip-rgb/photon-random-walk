import numpy as np
import random

pi =3.14159265

def gaussian(avg, std_dev):
    x = random.random()
    return (1 / (std_dev * np.sqrt(2 * pi))) * np.exp(
        -0.5 * ((x - avg) / std_dev)**2)