#------ 1 задание ------
def func1(year=1):
    """
        Функция, определяющая високосвный год
    """
    if year%4 != 0:
        print ("Обычный год")
    elif year%100 == 0:
        if year%400 == 0:
            print("Високосный")
    else:
        print("Обычный год")
func1(2000)
#------ 2 задание ------
import numpy as np
def func2(x):
    """
        Функция, перемножающая все элементы входного массива
    """
    s = 1
    for i in x:
        s = s*i
        
    return s

a = np.arange(1,10,1)
print(a)

print(func2(a))
#------ 3 задание ------
from const import falling
def func3(m,v,h):
    """
        Определение полного механического действия
    """

    energy = m*(v**2)/2+m*falling*h
    print(energy)
    
func3(1,23,4)
