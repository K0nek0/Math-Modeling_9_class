import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
import numpy as np
from scipy.integrate import odeint

seconds_in_year = 365*24*60*60
seconds_in_day = 24*60*60
years = 2

t = np.arange(0, years*seconds_in_year, seconds_in_day)

def Gravy(z,t):
    (x_venera, v_x_venera, y_venera, v_y_venera,
     x_saturn, v_x_saturn, y_saturn, v_y_saturn)= z
    dxdt_venera = v_x_venera
    dv_xdt_venera = -G * sun_mass * x_venera / (x_venera**2 + y_venera**2)**1.5
    dydt_venera = v_y_venera
    dv_ydt_venera = -G * sun_mass * y_venera / (x_venera**2 + y_venera**2)**1.5
    
    dxdt_saturn = v_x_saturn
    dv_xdt_saturn = -G * sun_mass * x_saturn / (x_saturn**2 + y_saturn**2)**1.5
    dydt_saturn = v_y_saturn
    dv_ydt_saturn = -G * sun_mass * y_saturn / (x_saturn**2 + y_saturn**2)**1.5

    return (dxdt_venera, dv_xdt_venera, dydt_venera, dv_ydt_venera,
            dxdt_saturn, dv_xdt_saturn, dydt_saturn, dv_ydt_saturn)
    
x0_venera = 108.2*10**9
vx0_venera = 0
y0_venera = 0
vy0_venera = 35000

x0_saturn = 0
vx0_saturn = 9690
y0_saturn = 142.9*10**10
vy0_saturn = 0

z0 = (x0_venera, vx0_venera, y0_venera, vy0_venera,
      x0_saturn, vx0_saturn, y0_saturn, vy0_saturn)

G = 6.67*10**(-11)
sun_mass = 1.9*10**30

sol = odeint(Gravy, z0, t)

fig = plt.figure()
planets = []

for i in range(0, len(t), 1):
    sun, = plt.plot([0], [0], 'yo', ms = 15)
    
    venera, = plt.plot(sol[:i, 0], sol[:i, 2], 'r-')
    venera_line, = plt.plot(sol[:i, 0], sol[:i, 2], 'ro')
    
    saturn, = plt.plot(sol[:i, 4], sol[:i, 6], 'g-')
    saturn_line, = plt.plot(sol[:i, 4], sol[:i, 6], 'go')
    
    planets.append([sun, venera, venera_line, saturn, saturn_line])
    
ani = ArtistAnimation(fig, planets, interval = 50)
plt.axis('equal')
ani.save('venera_and_saturn.gif')
    