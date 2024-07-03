import numpy as np 
from scipy.optimize import root
from math import e, log

f = lambda x : log(3-x)+x-2
f_prime = lambda x: -1*(3-x)**(-1)+1
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

print("f(r) = ", f(r.x))
print("f'(r) = ", f_prime(r.x))
f_prime_2 = lambda x: -1*(3-x)**(-2)
print("f''(r) =  ", f_prime_2(r.x))
f_prime_3 = lambda x: -2*(3-x)**(-3)
print("f'''(r) = ", f_prime_3(r.x))
