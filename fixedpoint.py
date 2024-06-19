import numpy as np
from math import e

n = int(input("input n value: "))
x_0 = float(input("input initial value: "))
p = int(input("input p value: "))

tol = 0.5 * 10**(-p)


def fixpoint(g, x_0, n):
    x_n = x_0
    for i in range(n):
        g_x_n = g(x_n)
        x_n_plus_1 = g(x_n)
        x_n = x_n_plus_1
    return g(x_n)

g = lambda x: (x-e**(x-2))**(1/3)

#print(fixpoint(g, x_0, n))
if np.abs(fixpoint(g, x_0, n) - fixpoint(g, x_0, n-1)) < tol:
    print(fixpoint(g, x_0, n))
else:
    print("out of tol")