import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(0 , 100, 0.1)

def shtuka(v, t):
    dvdt = (F - y*v**2)/m
    return dvdt

F = 100
y = 0.05
v_0 = 0
m = 100

solve = odeint(shtuka, v_0, t)
plt.plot(t, solve[0:,0])
plt.show()
