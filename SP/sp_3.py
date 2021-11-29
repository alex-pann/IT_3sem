import numpy as np
from scipy.integrate import odeint
from sympy import symbols, Function, Eq, solve, dsolve, latex
from math import sqrt
import matplotlib.pyplot as plt

# символьное решение SymPy
x = symbols('x')
y = symbols('y', cls=Function) # объявление символьной функции
diffeq = Eq(y(x).diff(x), -2*y(x)) 
res = dsolve(diffeq, y(x)) # общее решение
print(res)

C1 = symbols("C1")
seq = solve(res.subs({x : 0, y(x) : sqrt(2)}))
res = res.subs({C1: seq[0]}).evalf(4) # чатное решение
print("Решение, найденное SymPy-ем: ", latex(res))

func = []
t = np.arange(0, 10, 0.1)
for i in t:
    p = float(solve(res.subs({x : i}))[0][y(i)])
    func.append(p)  

#численное решение SciPy
def dydt(f, x):
    return -2*f

x = np.arange(0, 10, 0.1)
f0 = sqrt(2)
f = odeint(dydt, f0, x)    # решение уравнения 
f = np.array(f).flatten()    # преобразование массива 

fig, ax = plt.subplots(3, 1, figsize=(12, 8))

ax[0].plot(t, func, 'r-', linewidth=1) 
ax[0].grid(which = 'major', color='gray', linestyle='--', linewidth=0.3)
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')

ax[1].plot(x, f,'-',linewidth=1)
ax[1].grid(which = 'major', color='gray', linestyle='--', linewidth=0.3)
ax[1].set_xlabel('x')
ax[1].set_ylabel('y')

ax[2].plot(x, f - func, '-',linewidth=1)
ax[2].grid(which = 'major', color='gray', linestyle='--', linewidth=0.3)
ax[2].set_xlabel('x')
ax[2].set_ylabel('SciPy - SymPy')
plt.savefig("sp_3_result.png")
plt.show()