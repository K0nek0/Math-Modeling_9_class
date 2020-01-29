import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(10**(-7), 1.1*10**(-7), 10**(-11))

def smthing(s, t):
    x, v_x, y, v_y, z, v_z = s
    dxdt = v_x
    dv_xdt = q/m * (Ex + v_y*Bz - By*v_z)
    dydt = v_y
    dv_ydt = q/m * (Ey + v_z*Bx - Bz*v_x)
    dzdt = v_z
    dv_zdt = q/m * (Ez + v_x*By - Bx*v_y)
    return dxdt, dv_xdt, dydt, dv_ydt, dzdt, dv_zdt

x0 = 0
v_x0 = 10**7

y0 = 0
v_y0 = 10**6

z0 = 0
v_z0 = 0

s0 = x0, v_x0, y0, v_y0, z0, v_z0

m = 1.6*10**(-31)
q = 1.6*10**(-19)

Ex = 0
Ey = 10**(-3)
Ez = 0

Bx = 0
By = 10**(-3)
Bz = 0

sol = odeint(smthing, s0, t)

fig = plt.figure()
ax = fig.gca(projection = '3d')

ax.plot(sol[:, 0], sol[:, 2], sol[:, 4], label = 'electron')

ax.quiver(x0, y0, z0, Bx, By, Bz, length = 0.035,
          normalize = True, color = 'r', label = 'B')

ax.quiver(x0, y0, z0, Ex, Ey, Ez, length = 0.035,
          normalize = True, color = 'g', label = 'E')

ax.quiver(x0, y0, z0, v_x0, v_y0, v_z0, length = 0.035,
          normalize = True, color = 'k', label = 'v')

ax.legend()

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
