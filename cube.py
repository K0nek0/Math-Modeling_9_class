#import numpy as np
import matplotlib.pyplot as plt
def cube(a=1):
    '''
        Функция по созданию куба
    '''
    
    plt.plot([a,a,a+a,a+a,a],[a,a+a,a+a,a,a],color='k',marker='o',ms=5)
    plt.plot([2*a,2.5*a,2.5*a,1.5*a,a],[a,1.5*a,2.5*a,2.5*a,2*a],color='k',marker='o',ms=5)
    plt.plot([2*a,2.5*a],[2*a,2.5*a],color='k',marker='o',ms=5)
    plt.plot([1.5*a,1.5*a,1.5*a],[2.5*a,2.5*a,1.5*a],linestyle='--',linewidth=1)
    plt.plot([2*a],[1.5*a],linestyle='--',linewidth=1)
    plt.plot([2.5*a,1.5*a,a],[1.5*a,1.5*a,a],linestyle='--',linewidth=1)
    plt.axis('equal')
    plt.show()

cube(1)