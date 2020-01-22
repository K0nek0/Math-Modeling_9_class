import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

t=np.arange(0,100,0.1)

def strong(z,t):
    x,v_x,y,v_y = z
    dxdt = v_x
    dv_xdt = (F1 + F2*np.cos(A) + F3*np.cos(2*A) + F4*np.cos(3*A))/m
    dydt = v_y
    dv_ydt = (F4 + F3*np.sin(A) + F2*np.sin(2*A) + F1*np.sin(3*A))/m
    return dxdt, dv_xdt, dydt, dv_ydt

x0 = 0
v_x0 =-10
y0 = 0
v_y0 = -30
z0 = x0, v_x0, y0, v_y0

F1 = 10
F2 = 10
F3 = 10
F4 = 10
m = 50
A = 0.5235987756
sol = odeint(strong, z0, t)

fig = plt.figure()
strong = []

for i in range(0, len(t), 1):
    Fas, = plt.plot(sol[:i,0] ,sol[:i,2], '-', color='r')
    Fas_line, = plt.plot(sol[i,0], sol[i,2], 'o', color='r')
    strong.append([Fas, Fas_line])
    
ani=ArtistAnimation(fig, strong, interval=30)
plt.axis('equal')
ani.save('sily.gif')
