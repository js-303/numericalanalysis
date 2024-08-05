import numpy as np 
from scipy.optimize import root
import matplotlib.pyplot as plt
from numpy import linspace
from math import e, log, pi, sin, cos

f = lambda x : e**((sin(x))**3)+x**6-2*x**4-x**3-1
f_prime = lambda x: (3*cos(x)*(sin(x))**2)*e**((sin(x))**3)+6*x**5-8*x**3-3*x**2
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
print("estimate =", np.round(estimate, p))


r = root(f, x_0)
print("root: ", np.round(r.x, p))
f_error = abs(np.round((r.x - estimate), p))
print("forward error: ", f_error)
b_error = abs(np.round(f(estimate), p))
print("backward error: ", b_error)

f_v = np.vectorize(f)
x = linspace(-pi, pi)
plt.plot(x, f_v(x), 'b')
plt.show()



print("f(r) = ", f(r.x))
print("f'(r) = ", f_prime(r.x))

"""
f_prime_2 = lambda x: (20/3)*pi+4*pi*x_0
print("f''(r) =  ", f_prime_2(r.x))
f_prime_3 = lambda x: 
print("f'''(r) = ", f_prime_3(r.x))
"""
