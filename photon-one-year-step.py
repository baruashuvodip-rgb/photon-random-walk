import numpy as np
import random

radius = 696000000 #radius of the sun in meters

num_particles = int(input("Enter the number of particles to simulate: "))
exit_time = []
for i in range(num_particles):
    position = 0.0
    time = 0.0
    while(position**2<=radius**2):
        x = random.normalvariate(0.0, 320000) #random displacement of photon in 1 year
        position +=x
        time += 1.0
    exit_time.append(time)

avg_time = np.mean(exit_time)
std_time = np.std(exit_time)

print(f"Average time for photons to exit the sun: {avg_time} years")
print(f"Standard deviation of exit time: {std_time} years")


#doing this for 4.6 million years would require nearly 200 days of computation time on my machine, so I will not do that.