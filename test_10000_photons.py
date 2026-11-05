import numpy as np

from read_dat import read_data

x, y, z, s = read_data()

avg_x = np.mean(x)
std_x = np.std(x)

print(f"Average 1D distance travelled by photons: {avg_x}")
print(f"Standard deviation of 1D distances travelled by photons: {std_x}")

rms_distance = np.sqrt(np.mean(x**2))

print(f"RMS 1D distance travelled by photons: {rms_distance}")

#results are similar to gaussian_step.py, but off by some magnitude. different units?

'''import matplotlib.pyplot as plt
plt.hist(x, bins='fd', label="avg dist")
plt.xlabel("distance travelled in 1 second")
plt.ylabel("Number of photons")
plt.show()'''

#3d distance is not a gaussian distribution. the peak is skewed to the left with a long tail to the right.
#1d distance is essentially a gaussian distribution, with only a slight skew to the left.