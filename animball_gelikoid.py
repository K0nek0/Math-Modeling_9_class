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

x1 = phi * np.cos(theta)
y1 = phi * np.sin(theta)
z1 = h * theta

ball, = ax.plot(x1, y1, z1, 'o', color = 'b', ms=10)
line, = ax.plot(x1, y1, z1, '-', color = 'b')

def animation_func(i):
    ball.set_data(x1[i], y1[i])
    ball.set_3d_properties(z1[i])
    
    line.set_data(x1[:i], y1[:i])
    line.set_3d_properties(z1[:i])
    

ani = animation.FuncAnimation(fig, animation_func, 100, interval = 50)
ani.save('animball_gelikoid.gif')
