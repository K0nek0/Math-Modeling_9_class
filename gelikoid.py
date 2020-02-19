import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

fig = plt.figure()
ax = p3.Axes3D(fig)

phi = np.linspace(0, np.pi*2, 100)
theta = np.linspace(0, np.pi*7, 100)

h = 10

x = np.outer(phi, np.cos(theta))
y = np.outer(phi, np.sin(theta))
z = h * np.outer(np.ones(np.size(phi)), theta)

ax.plot_surface(x, y, z, color = 'g')
plt.show()
