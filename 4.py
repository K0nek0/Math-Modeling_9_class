import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

R = 10
N = 10
v = 5
x0 = 0
y0 = 0

def balls (R, N, v, x0, y0):
    alpha = 360/N
    
    coordinate = np.ndarray(shape=(N, 2))    
    velocity = np.ndarray(shape=(N, 2))
    
    for i in range(N):
        x = R * np.cos(i * alpha * np.pi/180)
        y = R * np.sin(i * alpha * np.pi/180)
        
        plt.plot(x, y, marker = 'o')
        
        coordinate.append[i][0] = x
        coordinate.append[i][0] = y
        
        if x <= 0 and y <= 0:
            v_x = -v * np.cos(i * alpha)
            v_y = -v * np.sin(i * alpha)
            
        elif x <= 0 and y >= 0:
            v_x = -v * np.cos(i * alpha)
            v_y = v * np.sin(i * alpha)
            
        elif x >= 0 and y <= 0:
            v_x = v * np.cos(i * alpha)
            v_y = -v * np.sin(i * alpha)
            
        elif x >= 0 and y >= 0:
            v_x = v * np.cos(i * alpha)
            v_y = v * np.sin(i * alpha)
        
        velocity.append[i][0] = v_x
        velocity.append[i][i] = v_y
        
    plt.axis('equal')
    plt.xlim(-2*R, 2*R)
    plt.ylim(-2*R, 2*R)
    plt.show()
    
    return coordinate, velocity

x, y, v_x, v_y  = balls(R, N, v, x0, y0)
