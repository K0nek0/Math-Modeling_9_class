from sympy import * 

L = Function('L')
phi_1 = Function('phi_1')
phi_2 = Function('phi_2')
v_phi_1 = Function('v_phi_1')
v_phi_2 = Function('v_phi_2')

t = Symbol('t')

m_1 = Symbol('m_1')
m_2 = Symbol('m_2')

l_1 = Symbol('l_1')
l_2 = Symbol('l_2')

g = Symbol('g')

L = m_1 * m_2 * l_1**2 * v_phi_2(t)**2 / 2 + m_2 * l_2**2 * v_phi_2(t)**2 + m_2 * l_1 * l_2 * v_phi_1(t) * v_phi_2(t) * cos(phi_1(t) - phi_2(t)) + (m_1 + m_2) * g * l_1 * cos(phi_1(t)) + m_2 * g * l_2 * cos(phi_2(t))

print(diff(L, phi_1(t)))
print()
print(diff(diff(L, v_phi_1(t)), t))
print()
print(diff(L, phi_2(t)))
print()
print(diff(diff(L, v_phi_2(t)), t))

