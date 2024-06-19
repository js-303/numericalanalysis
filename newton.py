import numpy as np 
from math import e

f = lambda x: ((x*2+1)/(x+1))-3*x
f_prime = lambda x: ((x**2+2*x-1)/(x+1)**2)-3
x_0 = float(input("input initial guess(int): "))
p = int(input("correct to how many decimal places(int): "))
tol = 0.5 * 10**(-p)

newton_raphson = x_0 - (f(x_0))/(f_prime(x_0))
print("newton_raphson =", newton_raphson)

def newton(f, df, x_0, tol):
    if abs(f(x_0)) < tol:
        print(x_0)
        return x_0
    else:
        return newton(f, df, x_0 - f(x_0)/df(x_0), tol)

estimate = newton(f, f_prime, x_0, tol)
print("estimate =", estimate)