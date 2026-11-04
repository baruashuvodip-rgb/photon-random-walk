import gaussian_step as gstep
import numpy as np

steps = int(input("Enter the number of steps to take: "))
particles = int(input("Enter the number of particles to simulate: "))

if particles==1:
    x,y,z = gstep.step_np(steps)

    x_total = np.sum(x)
    y_total = np.sum(y)
    z_total = np.sum(z)

    distance_travelled = np.sqrt(x_total**2 + y_total**2 + z_total**2)

    print(f"Distance travelled by particle: {distance_travelled} meters")

else:
    s = []
    for i in range(particles):
        x,y,z = gstep.step_np(steps)

        x_total = np.sum(x)
        y_total = np.sum(y)
        z_total = np.sum(z)

        s.append(np.sqrt(x_total**2 + y_total**2 + z_total**2))
        
    avg_distance = np.mean(s)
    std_distance = np.std(s)
    print(f"Average distance travelled by particles: {avg_distance} meters")
    print(f"Standard deviation of distance travelled: {std_distance} meters")

    rms_distance = np.sqrt(np.mean(s**2))
    print(f"RMS distance travelled by particles: {rms_distance} meters")

    #import matplotlib.pyplot as plt
    #plt.hist(avg_distance, bins='fd', label="avg dist")
    #plt.xlabel("distance travelled in 0.01 second")
    #plt.ylabel("Number of photons")
    #plt.show()

#with open("gaussian_step.txt", "w") as f:
    #for i in range(len(x)):
        #f.write(f"{i} {x[i]} {y[i]} {z[i]}\n")

#x_avg = np.mean(x)
#y_avg = np.mean(y)
#z_avg = np.mean(z)

#x_std = np.std(x)
#y_std = np.std(y)
#z_std = np.std(z)

#print(x_avg, y_avg, z_avg)    
#print(x_std, y_std, z_std)

#this code took 2.1350988 seconds to run on my machine, much longer than the 1 second it is supposed to be modelling


