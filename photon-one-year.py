import numpy as np

def step(mu,sigma):
    x = np.random.normal(loc=mu,scale=sigma, size = 365*86400) # 1 year of seconds
    y = np.random.normal(loc=mu,scale=sigma, size = 365*86400)
    z = np.random.normal(loc=mu,scale=sigma, size = 365*86400)
    return x,y,z

x, y, z = step(99.994757, 57.732) # mean and std dev of 1D distance travelled by photons in 1 second
total_x = np.sum(x)
total_y = np.sum(y)
total_z = np.sum(z)

s = np.sqrt(total_x**2 + total_y**2 + total_z**2)

print(f"Distance travelled by photons in 1 year: {s} meters")