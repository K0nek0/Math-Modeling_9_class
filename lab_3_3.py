import numpy as np
from const import falling
x0 = 0
y0 = 0
v0 = 0
t=np.arange(0,5,0.01)
n=len(t)
txy=np.ndarray(shape=(n,3))
for i in range(0,n,1):
    x = x0 + v0*t[i]
    y = y0 + v0*t[i]-(falling*t[i]**2)/2
    txy[i,0]=x
    txy[i,1]=y
    txy[i,2]=t[i]
print (txy)
