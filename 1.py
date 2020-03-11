from sympy import * 
import numpy as np

L = Function('L')
v_phi = Function('v_phi')
phi = Function('phi')


t = Symbol('t')
m = Symbol('m')
l = Symbol('l')
R = Symbol('R')
omega = Symbol('omega')
g = Symbol('g')

L = m*l**2*v_phi(t)**2/2 + m*R*l*omega**2*cos(phi(t)-omega*t) + m*g*l*cos(phi(t))

print(diff(L, phi(t)))
print()
print(diff(L, v_phi(t)))
print()
print(diff(diff(L, v_phi(t)), t))
