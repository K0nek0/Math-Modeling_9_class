import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation

N = 200
t = np.linspace(0, 1, N)

a = 1
b = 1
c = 1

g = 9.8

def move(s, t):
    x, v_x, y, v_y, z, v_z = s
    
    lyam = g - (v_x**2 / a**2) - (v_y**2 / b**2) - (v_z**2 / c**2) / (x**2 / a**4) + (y**2 / b**4) + (z**2 / c**4)
    
    dxdt = v_x
    dvxdt = x*lyam / a**2
    
    dydt = v_y
    dvydt = y*lyam / b**2
    
    dzdt = v_z
    dvzdt = -g + x*lyam / a**2
    
    return dxdt, dvxdt, dydt, dvydt, dzdt, dvzdt

#lyam = g - (v_x**2 / a**2) - (v_y**2 / b**2) - (v_z**2 / c**2) / (x**2 / a**4) + (y**2 / b**4) + (z**2 / c**4)

x0 = 1
v_x0 = 0

y0 = 1
v_y0 = 0

z0 = 1
v_z0 = 0

s0 = x0, v_x0, y0, v_y0, z0, v_z0


sol = odeint(move, s0, t)

fig = plt.figure()
ax = p3.Axes3D(fig)

x1 = sol[:, 0]
y1 = sol[:, 2]
z1 = sol[:, 4]

body1, = ax.plot(x1, y1, z1, 'o', color = 'r')
body1_line = ax.plot(x1, y1, z1,  '-', color = 'r')
    
def animation_func(i):
    
    body1.set_data(x1[i], y1[i])
    body1.set_3d_properties(z1[i])
    
    body1_line.set_data(x1[:i], y1[:i])
    body1_line.set_3d_properties(z1[:i])
    
    
ani = animation.FuncAnimation(fig, animation_func, N, interval = 50)
ani.save('1.gif')
