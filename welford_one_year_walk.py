import numpy as np
mean = 0.0
M_2 = 0.0
for i in range(1000): #random walk for 1000 particles

    x = np.random.normal(loc=0.0,scale=57.732, size = 31536000) # mean and std dev of 1D distance travelled by photons in 1 second
    total_x = np.sum(x)
    old_mean = mean
    mean += (total_x - old_mean)/(i+1)
    M_2 += (total_x - old_mean)*(total_x - mean)
    variance = M_2/(i+1)

std_dev = np.sqrt(variance)

print(f"Standard deviation of distance travelled by photons in 1 year: {std_dev} meters")

    