import numpy as np  
from math import e

f = lambda x : 27*x**3+54*x**2+36*x+8
f_prime = lambda x: 81*x**2+108*x+36
x_0 = float(input("input initial guess(float): "))
p = int(input("accurate to how many decimal places(int): "))
tol = 0.5 * 10**(-p)
m = int(input("times continuously differentiable minus 1: "))

def modifiednewton(f, df, x_0, tol):
    if abs(f(x_0)) < tol:
        return x_0
    else:
        return modifiednewton(f, df, x_0-m*(f(x_0)/df(x_0)), tol)

estimate = modifiednewton(f, f_prime, x_0, tol)
print("estimate =", round(estimate, p))

coef = [27, 54, 36, 8]
r = np.roots(coef)
print(r)
f_error = abs(r - estimate)
print("forward error: ", f_error)
b_error = abs(f(estimate))
print("backward error: ", b_error)