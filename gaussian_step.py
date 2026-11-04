import numpy as np

def step_np(N):
    x = np.random.normal(loc=0.0,scale=0.00577,size=N)
    y = np.random.normal(loc=0.0,scale=0.00577,size=N)
    z = np.random.normal(loc=0.0,scale=0.00577,size = N)
    return x,y,z

