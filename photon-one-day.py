import numpy as np

def step(mu,sigma):
    x = np.random.normal(loc=mu,scale=sigma, size = 86400) # 1 day of seconds
    return x
total_x = []

for i in range(100000): 
    x = step(0.0, 57.732) # mean and std dev of 1D distance travelled by photons in 1 second
    total_x.append(np.sum(x))

std_distance = np.std(total_x)

print(f"Standard deviation of distance travelled by photons in 1 day: {std_distance} meters")

