import numpy as np
import math
from math import e
import matplotlib.pyplot as mp

def my_bisection(f, a, b, tol):
    
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("a and b do not bound r")

    m = (a + b)/2
    
    if np.abs(f(m)) < tol:
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        return my_bisection(f, m, b, tol)
    elif np.sign(f(b)) == np.sign(f(m)):
        return my_bisection(f, a, m, tol)

f = lambda x: 2*(x**3)-6*(x)-1
p = int(input("input decimal places the solution is correct within(integer): "))
a = float(input("input lower bound of interval(int): "))
b = float(input("input upper bound of interval(int): "))
tol = 0.5 * 10**(-p)
r1 = my_bisection(f, a, b, tol)
print("r = ", r1)

n = -(1+math.log2(tol))-math.log2(b-a)
steps = math.ceil(n)
print("number of steps: ", steps)
print(type(f))
