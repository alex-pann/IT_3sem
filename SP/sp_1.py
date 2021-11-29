import numpy as np
from sympy import *

r, l, m = symbols('ρ λ μ')

n = 9
A = np.zeros(n)
P = np.diag([-1/r, -1/r, -1/r, 0, 0, 0], 3)
M = np.diag([-(l+2*m), -m, -m, 0, 0, 0], -3)
A = A+P+M
A[6, 0] = -l
A[8, 0] = -l
A = Matrix(A)
print(A.eigenvals())