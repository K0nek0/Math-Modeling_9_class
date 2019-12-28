import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(0, 200, 0.01)

def dif_mm(z, t):
    S, v = z
    dS_dt = v
    dv_dt = -g*np.sin(S/l)-k/m*v
    return dS_dt, dv_dt

g = 10
l = 10
m = 10
k = 0.1

S0 = 5
v0 = 0
z0 = S0, v0

sol = odeint(dif_mm, z0, t)
plt.plot(t, sol[:,1])
plt.show()
