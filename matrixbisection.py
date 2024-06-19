import numpy as np
import math

def det_bisection(A, a, b, tol):
    
    if np.sign(detA(a)) == np.sign(detA(b)):
        raise Exception("a and b do not bound r")

    m = (a + b)/2
    
    if np.abs(detA(m)) < tol:
        return m
    elif np.sign(detA(a)) == np.sign(detA(m)):
        return det_bisection(A, m, b, tol)
    elif np.sign(detA(b)) == np.sign(detA(m)):
        return det_bisection(A, a, m, tol)

A = lambda x: np.matrix([[1,2,3,x],[4,5,x,6],[7,x,8,9],[x,10,11,12]])
detA = lambda x: np.linalg.det(A(x))-1000

p = int(input("input decimal places the solution is correct within(int): "))
a = float(input("input lower bound of the interval(float): "))
b = float(input("input upper bound of the interval(float): "))
tol = 0.5 * 10**(-p)
n = -1-math.log2(tol)+math.log2(b-a)
steps = math.ceil(n)

x1 = det_bisection(A, a, b, tol)
print("x1 =", x1)