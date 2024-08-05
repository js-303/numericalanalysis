import numpy as np
import numpy.linalg as la
from numpy import array, inf, zeros_like, empty

A = array([[2,-2,-1],
           [4,1,-2],
           [-2,1,-1]], dtype=float)
b = array([-2,1,-3], dtype=float)


def rowreduce(A, b):
    U = A.copy()
    c = b.copy()
    n = len(b)

    L = zeros_like(A)
    for k in range(n):
        for i in range(k+1, n):
            L[i,k] = U[i,k]/U[k,k]
            print(L[i,k])
            for j in range(k+1, n):
                print(j)
                U[i,j] -= L[i,k]*U[k,j]
                U[i,k] = 0
                c[i] -= L[i,k]*c[k]
                print(U)
    return (U,c)

"""
def backsub(A, b):
    U = A.copy()
    c = b.copy()
    n = len(c)
    x = np.zeros(n)
    x[n-1] = c[n-1]/U[n-1,n-1]
    for i in range(n-2, -1, -1):
        x[i] = (c[i] - sum(U[i,i+1:] * x[i+1:])) / U[i,i]
    return x
"""
print(rowreduce(A,b))
print(la.solve(A,b))
