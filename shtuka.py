import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

fig = plt.figure()

def circle(xc_centre_point, yc_centre_point, R, N):
    x = np.zeros(N)
    y = np.zeros(N)
    for i in range(0, N, 1):
        alpha = np.linspace(0, 2*np.pi, N)
        x[i] = xc_centre_point + R*np.cos(alpha[i])
        y[i] = yc_centre_point + R*np.sin(alpha[i])
        
    return x, y

a = 1
R = 20

anim_list = []
N = 100

xc = np.linspace(-5, 5, N)
yc = a*xc**2

for i in range(0, N, 1):
    x, y = circle(xc[i], yc[i], R=R, N=N)
    circle1, = plt.plot(x, y)

    anim_list.append([circle1])

plt.axis('equal')
ani = ArtistAnimation(fig, anim_list, interval = 50)
ani.save("shtuka.gif")
