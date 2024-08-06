import numpy as np
import numpy.linalg as la
from numpy import array, inf, zeros_like, empty

A = array([[2,1,-4],
           [1,-1,1],
           [-1,3,-2]], dtype=float)
b = array([-7,-2,6], dtype=float)

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

(U, c) =rowreduce(A,b)


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

(U, c) =rowreduce(A,b)
print(U)
x = backsub(U,c)
print(f"x = {x}")
r = b - A@x
print(f"residual b - Ax = {r}")
print(f"max norm {max(abs(r)):.3}")
print(la.solve(A,b))

