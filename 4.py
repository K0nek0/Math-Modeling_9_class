import numpy as np
import matplotlib.pyplot as plt

R = 2
N = 20
v = 1
x0 = 0
y0 = 0

def func(R, N, v, x0, y0):
    coordinate = np.ndarray(shape=(N,2))
    velocity = np.ndarray(shape=(N,2))
    alpha = 360 / N * np.pi / 180
    
    for i in range(N):
        x = R * np.cos(i * alpha)
        y = R * np.sin(i * alpha)
        
        coordinate[i][0] = x+x0
        coordinate[i][1] = y+y0
        
        if x <= 0 and y <= 0:
            v_x = -v * np.cos(i * alpha)
            v_y = -v * np.sin(i * alpha)
            
        elif x <= 0 and y >= 0:
            v_x = -v * np.cos(i * alpha)
            v_y = v * np.sin(i * alpha)
            
        elif x >= 0 and y == 0:
            v_x = v * np.cos(i * alpha)
            v_y = -v * np.sin(i * alpha)
            
        elif x >= 0 and y >= 0:
            v_x = v * np.cos(i * alpha)
            v_y = v * np.sin(i * alpha)
            
#        if x < 0 and y < 0:
#            v_x = - v * np.cos(np.pi - alpha)
#            v_y = - v * np.sin(alpha)
#        elif x < 0 and y >= 0:
#            v_x = - v * np.cos(alpha)
#            v_y = v * np.sin(alpha)
#        elif x >= 0 and y >= 0:
#            v_x = v * np.cos(alpha)
#            v_y = v * np.sin(alpha)
#        elif x >= 0 and y < 0:
#            v_x = v * np.cos(alpha)
#            v_y = - v * np.sin(alpha)
        
        velocity[i][0] = v_x
        velocity[i][1] = v_y

        plt.plot(coordinate[i][0], coordinate[i][1], marker = 'o')
        plt.arrow(coordinate[i][0], coordinate[i][1], velocity[i][0], velocity[i][1])
    
    plt.axis('equal')
    plt.show()
    
    return coordinate, velocity
    
c, v = func(R, N, v, x0, y0)
