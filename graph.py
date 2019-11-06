import matplotlib.pyplot as plt
def square (x,y):
    """
        Функция по созданию квадрата по заданным координатам
    """
    plt.plot(x,y,color='k',marker='o',ms=15)
    plt.show()

x=[1,1,5,5,1]
y=[1,5,5,1,1]
square(x,y)