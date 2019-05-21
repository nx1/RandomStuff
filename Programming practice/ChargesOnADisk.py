import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(num=1)

DISK_RADIUS = 1
print(DISK_RADIUS)
x = np.arange(0,5,1)
y = np.arange(0,5,1)
plt.plot(x,y)
plt.Circle((0,0), radius=DISK_RADIUS )
plt.show()