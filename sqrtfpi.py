import numpy as np

a = 
x_0 = 
n = 
p = 
tol = 0.5 * 10***(-p)

def sqrtfpi(x_0, a, n):
    x_i = x_0
    for i in range(n):
        x_i_plus_1 = ((x_i + (a/x_i))/2)
        x_i = x_1_plus_1
    return x_i_plus_1

if np.abs(sqrtfpi(x_0, a, n) - sqrtfpi(x_0, a, n-1)) < tol:
    print(sqrtfpi(x_0, a, n))
else:
    print("out of to")