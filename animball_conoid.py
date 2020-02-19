import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation

fig = plt.figure()
ax = p3.Axes3D(fig)

phi = np.linspace(0, np.pi*2, 100)
theta = np.linspace(0, np.pi*4, 100)
h = 10

x = np.outer(phi, np.cos(theta))
y = np.outer(phi, np.sin(theta))
z = h * np.outer(np.ones(np.size(phi)), theta)

ax.plot_surface(x, y, z, color = 'g')

ball, = ax.plot(x, y, z, 'o', color = 'b')
line, = ax.plot(x, y, z, '-', color = 'b')

def animation_func(i):
    ball.set_data(x[i], y[i])
    ball.set_3d_properties(z[i])
    
    line.set_data(x[:i], y[:i])
    line.set_3d_properties(z[:i])
    

ani = animation.FuncAnimation(fig, animation_func, h, interval = 50)
plt.show()
