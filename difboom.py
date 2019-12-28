import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(0, 2000, 0.01)

def dif_boom(z, t):
    R, v = z
    dR_dt = v
    dv_dt = - G*m2/R**2
    
    return dR_dt, dv_dt

m2 = 5.972*10**24
G = 6.67*10**(-11)

R0 = 6400000
v0 = 2000
z0 = R0, v0

sol = odeint(dif_boom, z0, t)

plt.plot(t, sol[:,0])
plt.show()
