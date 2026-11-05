import numpy as np
import matplotlib.pyplot as plt

# Read the three columns into separate arrays
x, y, z = np.loadtxt('random_walk_4mil.txt', unpack=True)

# Create three plots
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

# XY plane
ax[0].scatter(x, y, s=1)
ax[0].set_xlabel('X')
ax[0].set_ylabel('Y')
ax[0].set_title('XY Plane')
ax[0].set_aspect('equal')

# YZ plane
ax[1].scatter(y, z, s=1)
ax[1].set_xlabel('Y')
ax[1].set_ylabel('Z')
ax[1].set_title('YZ Plane')
ax[1].set_aspect('equal')

# XZ plane
ax[2].scatter(x, z, s=1)
ax[2].set_xlabel('X')
ax[2].set_ylabel('Z')
ax[2].set_title('XZ Plane')
ax[2].set_aspect('equal')

plt.tight_layout()
plt.show()