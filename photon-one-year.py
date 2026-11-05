import numpy as np

def step(mu,sigma):
    x = np.random.normal(loc=mu,scale=sigma, size = 365) # 1 year of seconds
    return x
total_x = []

for i in range(100000): 
    x = step(0.0, 16900) # mean and std dev of 1D distance travelled by photons in 1 second
    total_x.append(np.sum(x))

std_distance = np.std(total_x)

print(f"Standard deviation of distance travelled by photons in 1 year: {std_distance} meters")


#doing this for 4.6 million years would require nearly 200 days of computation time on my machine, so I will not do that.