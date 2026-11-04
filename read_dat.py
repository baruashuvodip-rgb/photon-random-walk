import numpy as np

def read_data():
    data = np.loadtxt("photonDistances2.dat")

    x = data[:, 0]
    y = data[:, 1]
    z = data[:, 2]
    s = data[:, 3]
    return x, y, z, s