import numpy as np

def step_np(mu,sigma,N):
    x = np.random.normal(loc=mu,scale=sigma,size=N)
    y = np.random.normal(loc=mu,scale=sigma,size=N)
    z = np.random.normal(loc=mu,scale=sigma,size=N)
    return x,y,z

# simulate random walk over 1 second

x, y, z = step_np(0.0, 0.00577, 100000000)
x_coord = np.cumsum(x)
y_coord = np.cumsum(y)
z_coord = np.cumsum(z)
# modelling the random distance travelled by a photon between collisions, with 10^8 steps per second
s = np.sqrt(x**2 + y**2 + z**2) # distance travelled by photon in each step
with open("random_walk_1s.txt", "w") as f:
    for i in range(0, 100000000, 10000):
        f.write(f"{x_coord[i]} {y_coord[i]} {z_coord[i]}\n")

# simulate random walk over 1 year using 1 second steps

x, y, z = step_np(0.0, 57.732, 31536000)
x_coord = np.cumsum(x)
y_coord = np.cumsum(y)
z_coord = np.cumsum(z)
# modeling the random distance travelled by a photon each second, with 3.1536e7 steps per year
s = np.sqrt(x**2 + y**2 + z**2) # distance travelled by photon in each second
with open("random_walk_1y.txt", "w") as f:
    for i in range(0, 31536000, 1000):
        f.write(f"{x_coord[i]} {y_coord[i]} {z_coord[i]}\n")

# simulate random walk over 4.6 billion years using 1 year steps

x, y, z = step_np(0.0, 320000, 4500000)
x_coord = np.cumsum(x)
y_coord = np.cumsum(y)
z_coord = np.cumsum(z)
# modeling the random distance travelled by a photon each year, 
# with 4.5e6 steps for the 4.5 million years it takes for the photon to exit the radius of the sun
s = np.sqrt(x**2 + y**2 + z**2) # distance travelled by photon in each year
with open("random_walk_4mil.txt", "w") as f:
    for i in range(0, 4500000, 1000):
        f.write(f"{x_coord[i]} {y_coord[i]} {z_coord[i]}\n")