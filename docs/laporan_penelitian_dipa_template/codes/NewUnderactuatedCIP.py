import sympy as sp
from sympy.physics.mechanics import *
init_vprinting() 


# create symbolic variables
m, M, g, l, t, u, b1, b2, U, L, T = \
    sp.symbols('m M g l t u b_1 b_2 U L T')

# dynamic symbols have implicit dependence on time
theta, xM, yM, xm, ym = dynamicsymbols('theta x_M y_M x_m y_m')

xm = xM - l*sp.sin(theta)
ym = l * sp.cos(theta)

# Derivative
xm_dot = sp.diff(xm, t)
ym_dot = sp.diff(ym, t)

theta_dot = sp.diff(theta, t)
theta_ddot = sp.diff(theta_dot, t)

xM_dot = sp.diff(xM, t)
xM_ddot = sp.diff(xM_dot, t)

sp.pprint(xm_dot)
sp.pprint(ym_dot)
sp.pprint(theta_dot)
sp.pprint(theta_ddot)
sp.pprint(xM_dot)
sp.pprint(xM_ddot)

# Potential Energy
U = m*g*ym

# Kinetic Energy
T = (1/2)*M*xM_dot**2 + (1/2)*m*(xm_dot**2 + ym_dot**2).simplify()

# Lagrange
L = T - U
L = sp.expand(L)
sp.pprint(sp.collect(L, xM))
sp.pprint(sp.diff(L,xM_dot))
sp.pprint(sp.diff(sp.diff(L,xM_dot),t))
sp.pprint(sp.diff(L,xM))
sp.pprint(sp.diff(L,theta_dot))
sp.pprint(sp.diff(sp.diff(L,theta_dot),t))
sp.pprint(sp.diff(L,theta))

# Euler-Lagrange Equation
# solve the Euler-Lagrange Equations
f_3 = sp.diff( sp.diff(L,xM_dot), t).simplify() - \
    sp.diff(L, xM) + (b1*xM_dot) - u
f_4 = sp.diff( sp.diff(L,theta_dot), t).simplify() - \
    sp.diff(L, theta) + (b2*theta_dot)
f_3 = sp.simplify(f_3)
f_4 = sp.simplify(f_4)
sp.pprint(sp.collect(f_3, xM)) 
sp.pprint(sp.collect(f_4, theta))

sln3 = sp.solve([f_3], [xM_ddot], simplify=True)
sln4 = sp.solve([f_4], [theta_ddot], simplify=True)

expr3 = f_3.subs(theta_ddot, sln4[theta_ddot])
expr4 = f_4.subs(xM_ddot, sln3[xM_ddot])
sp.pprint(expr3) 
sp.pprint(expr4)
sln33 = sp.solve([expr3], [xM_ddot], simplify=True)
sln44 = sp.solve([expr4], [theta_ddot], simplify=True)
sp.pprint(sln33)
sp.pprint(sln44)
# show the solution
f = sp.Matrix([xM_dot, theta_dot, \
               sln33[xM_ddot],  sln44[theta_ddot]])
f = sp.simplify(f)
sp.pprint(f)