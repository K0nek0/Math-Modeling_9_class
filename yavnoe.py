import matplotlib.pyplot as plt
import numpy as np
def parabola(a=1,b=1,c=0):
    """
        Функция по созданию параболы
    """
    x=np.arange(-10,10,0.01)
    y=a*x**2+b*x+c
    plt.plot(x,y)
    plt.xlabel("coord-x")
    plt.ylabel("coord-y")
    plt.title("Явное задание кривых")
    plt.legend()
    plt.show()
parabola()

def giperbola(k):
    """
        Функция по созданию гиперболы
    """
    x=np.arange(0.01,10,0.01)
    y=k/x
    plt.plot(x,y)
    plt.show()
giperbola(0.03)
