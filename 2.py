import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

N = 300
t = np.linspace(0, 3, N)

def move_func(s, t):
    phi, v_phi = s
    
    dphi_dt = v_phi
    dvphi_dt = (R*omega**2*np.sin(omega*t-phi) - g*np.sin(phi)) / l
    
    return dphi_dt, dvphi_dt

phi0 = np.pi / 180*30
v_phi0 = 5
s0 = phi0, v_phi0

g = 9.8
R = 2
l = 1
omega = 2

sol = odeint(move_func, s0, t)

xR = R*np.sin(omega * t[:])
yR = -R*np.cos(omega * t[:])

x = xR + l*np.sin(sol[:, 0])
y = yR - l*np.cos(sol[:, 0])

fig = plt.figure()
bodys = []

for i in range(1, len(t), 1):
    tx = [0, xR[i], x[i]]
    ty = [0, yR[i], y[i]]
    
    body_line, = plt.plot(tx, ty, '-o', color = 'b')
    bodys.append([body_line])
    
ani = ArtistAnimation(fig, bodys, interval = 50)
plt.axis('equal')
plt.grid()

ani.save('shtuka.gif')
