import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection = '3d')

t = np.arange(0.01, 7*np.pi, 0.01)
R = 1

x = R*(np.cos(t))**3
y = R*(np.sin(t))**3
z = np.cos(2*t)

ax.plot(x, y, z)
ax.legend()

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
