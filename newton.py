import numpy as np 
from scipy.optimize import root
from math import e

f = lambda x : 2*e**(x-1)-x**2-1
f_prime = lambda x: 2*e**(x-1)-2*x
x_0 = float(input("input initial guess(int): "))
p = int(input("correct to how many decimal places(int): "))
tol = 0.5 * 10**(-p)

def newton(f, df, x_0, tol):
    if abs(f(x_0)) < tol:
        return x_0
    else:
        return newton(f, df, x_0 - f(x_0)/df(x_0), tol)

estimate = newton(f, f_prime, x_0, tol)
print("estimate =", np.round(estimate, p))

r = root(f, x_0)
print("root: ", np.round(r.x, p))
f_error = abs(np.round((r.x - estimate), p))
print("forward error: ", f_error)
b_error = abs(np.round(f(estimate), p))
print("backward error: ", b_error)