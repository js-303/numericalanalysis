import numpy as np
import numpy.linalg as la
from numpy import array, inf, zeros_like, empty
from fractions import Fraction as div

A = array([[div(1/1),div(1/2),div(1/3),div(1/4),div(1/5),div(1/6),div(1/7),div(1/8),div(1/9),div(1/10)],
           [div(1/2), div(1/3),div(1/4),div(1/5),div(1/6),div(1/7),div(1/8),div(1/9),div(1/10),div(1/11)],
           [div(1/3), div(1/4),div(1/5),div(1/6),div(1/7),div(1/8),div(1/9),div(1/10),div(1/11),div(1/12)],
           [div(1/4), div(1/5),div(1/6),div(1/7),div(1/8),div(1/9),div(1/10),div(1/11),div(1/12),div(1/13)],
           [div(1/5), div(1/6),div(1/7),div(1/8),div(1/9),div(1/10),div(1/11),div(1/12),div(1/13),div(1/14)],
           [div(1/6), div(1/7),div(1/8),div(1/9),div(1/10),div(1/11),div(1/12),div(1/13),div(1/14),div(1/15)],
           [div(1/7),div(1/8),div(1/9),div(1/10),div(1/11),div(1/12),div(1/13),div(1/14),div(1/15),div(1/16)],
           [div(1/8),div(1/9),div(1/10),div(1/11),div(1/12),div(1/13),div(1/14),div(1/15),div(1/16),div(1/17)],
           [div(1/9),div(1/10),div(1/11),div(1/12),div(1/13),div(1/14),div(1/15),div(1/16),div(1/17),div(1/18)],
           [div(1/10),div(1/11),div(1/12),div(1/13),div(1/14),div(1/15),div(1/16),div(1/17),div(1/18),div(1/19)],], dtype=float)
b = array([1,1,1,1,1,1,1,1,1,1], dtype=float)

def rowreduce(A, b):
    U = A.copy()
    c = b.copy()
    n = len(b)

    L = zeros_like(A)
    for k in range(n):
        for i in range(k+1, n):
            L[i,k] = U[i,k]/U[k,k]
            for j in range(k+1, n):
                U[i,j] -= L[i,k]*U[k,j]
            U[i,k] = 0
            c[i] -= L[i,k]*c[k]
    return (U,c)

(U, c) = rowreduce(A,b)


def backsub(U, c):
    n = len(c)
    x = np.zeros(n)
    x[n-1] = c[n-1]/U[n-1,n-1]
    for i in range(n-2, -1, -1):
        x[i] = (c[i] - sum(U[i,i+1:] * x[i+1:])) / U[i,i]
    return x
"""
def backsubdemo(U,c,demomode=False):
    n = len(c)
    x = np.zeros(n)
    x[-1] = c[-1]/U[-1,-1]
    if demomode: print(f"x_{n} = {x[-1]}")
    for i in range(2, n+1):
        x[-i] = (c[-i] - sum(U[-i, 1-i:] * x[1-i:])) / U[-i, -i]
        if demomode: print(f"x_{n-i+1} = {x[-i]}")
    return x
"""

print(U, c)
x = backsub(U,c)
print(f"x = {x}")
r = b - A@x
print(f"residual b - Ax = {r}")
print(f"max norm {max(abs(r)):.3}")
print(la.solve(A,b))

