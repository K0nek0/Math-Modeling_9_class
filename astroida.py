import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

anim_object, = plt.plot([],[], 'ro')

def astroida(r, t):
    
    x = r*np.cos(t)**3
    y = r*np.sin(t)**3
    return x, y

edge=4
ax.set_xlim(-edge,edge)
ax.set_ylim(-edge,edge)
plt.axis('equal')

def animate(i):
    anim_object.set_data(astroida(r=1, t=i))
    
ani=animation.FuncAnimation(fig,
                            animate,
                            frames=np.arange(-5, 100*np.pi, 0.1),
                            interval=20)

ani.save('astroida.gif')
