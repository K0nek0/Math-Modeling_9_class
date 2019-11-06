import matplotlib.pyplot as plt
import numpy as np
def ellips (a,b):
    """
        Функция по созданию эллипса
    """
    x=np.arange(-2.0,3.0,0.1)
    y=np.arange(-2.0,3.0,0.1)
    X,Y=np.meshgrid(x,y)
    fxy=X**2/a**2+Y**2/b**2-1
    plt.contour(X,Y,fxy,levels=[0])
ellips(2,1)

def circle(R=1):
    """
        Функция по созданию окружности
    """
    x=np.arange(-2.0,2.0,0.1)
    y=np.arange(-2.0,2.0,0.1)
    X,Y=np.meshgrid(x,y)
    fxy=X**2+Y**2
    plt.contour(X,Y,fxy,levels=[R])
circle(2)
