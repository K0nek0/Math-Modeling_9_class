import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig,ax = plt.subplots()

ball, = plt.plot([],[], 'ro')

def cicloida(Radius,t):
    
    x = Radius*(t-np.sin(t))
    y = Radius*(1-np.cos(t))
    return x,y

edge=10
ax.set_xlim(0, 3*edge)
ax.set_ylim(-edge, edge)
plt.axis('equal')

def animate(i):
    ball.set_data(cicloida(Radius=2, t=i))

ani=animation.FuncAnimation(fig,
                            animate,
                            frames=np.arange(0, 20*np.pi, 0.1),
                            interval=30)

ani.save('cicloida.gif')
