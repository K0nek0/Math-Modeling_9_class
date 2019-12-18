import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(0, 100, 1)

def bio(N, t):
    dNdt = k*N
    return dNdt

N_0 = 1
k = 0.05

solve = odeint(bio, N_0, t)

plt.plot(t, solve[:,0], label="Бактерии")
plt.show()
