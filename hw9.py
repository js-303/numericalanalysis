import numpy as np
import matplotlib.pyplot as plt

f = lambda x: x*np.exp(-x**2)
F = -np.exp(-9)/2+(1/2)
a = 0
b = 3
abs_err_values= []
panel_values = []
err_values = []
g = lambda n: ((b-a)/(2**n))**4 

def simpson(f, a, b, n):
  h = (b - a) / (2*n)
  xk = np.linspace(a, b, 2*n + 1)
  sum = f(xk[0]) + f(xk[-1])
  sum += 2*np.sum(f(xk[2:-1:2]))
  sum += 4*np.sum(f(xk[1:-1:2]))
  sum *= h/3
  return sum

"""
def comp_simp_err(a, b, n):
    h = (b - a) / (2*n)
    error = 
    return error
"""

for i in range(16):
    abs_error = abs(F-simpson(f, a, b, 2**i))
    abs_err_values.append(abs_error)
    panel_values.append(2**i)
    #err_values.append(comp_simp_err(a,b,2**i))

xx = np.linspace(0,15,1000)
plt.plot(xx, g(xx))
plt.semilogy(abs_err_values, 'o')
#plt.semilogy(err_values, 'o')
plt.yscale('log', base=2)
plt.show()


"""
def trapezoid(f, a, b, n):
  h = (b - a) / n
  xk = np.linspace(a, b, n + 1)
  sum = (h / 2) * (f(xk[0]) + 2 * np.sum(f(xk[1:-1])) + f(xk[-1]))
  return sum

def comp_trap_err(a, b, n):
    h = (b - a) / n
    error = ((b-a)*(h**2)/12)*90*np.exp(-9)
    return error

for i in range(16):
    abs_error = abs(F-trapezoid(f, a, b, 2**i))
    abs_err_values.append(abs_error)
    panel_values.append(2**1)
    err_values.append(comp_trap_err(a,b,2**i))

print(err_values)

xx = np.linspace(0,16,1000)
plt.plot(xx, g(xx))
plt.semilogy(abs_err_values, 'o')
plt.semilogy(err_values, 'o')
plt.yscale('log', base=2)
plt.show()
"""
