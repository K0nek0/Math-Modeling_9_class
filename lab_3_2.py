from const import falling
from math import tan,pi,cos,sqrt
h=100
B=pi/3
a=pi/5
v=sqrt(falling*h*1/(tan(B)**2)/(2*cos(a)**2*(1-1/tan(B)*tan(a))))
print("Ответ:" , v)
