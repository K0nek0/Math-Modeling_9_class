import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(0, 20, 0.01)

def dif(z,t):
    y, omega = z
    dy_dt = omega
    domega_dt = np.sin(-y)*omega-3*y*t-5
    
    return dy_dt, domega_dt

y0 = 0.01
omega0 = 0.05
z0 = y0, omega0

sol = odeint(dif, z0, t)

plt.plot(t, sol[:,0])
plt.plot(t, sol[:,1])
plt.plot(sol[:,1], sol[:,0])
plt.show()
