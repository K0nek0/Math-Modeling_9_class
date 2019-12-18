import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(0 , 15, 0.001)

def investicii(N, t):
    dNdt = -k*N*t
    return dNdt

N_0 = 1000
k = 0.08

solve = odeint(investicii, N_0, t)

plt.plot(t, solve[:,0])
plt.show()
