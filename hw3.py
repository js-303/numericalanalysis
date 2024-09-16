import numpy as np
import math



randcos = lambda x: np.cos(x) + np.random.normal(0, 0.1)

def bisect(f,a,b,N,xtol):
  '''
  f: function
  a: left endpoint of the interval
  b: right endpoint of the interval
  N: maximal number of iterations
  xtol: tolerance for the length of the interval
  '''

  fa = randcos(a)
  fb = randcos(b)
  for i in range(N):
    c = (a+b)/2
    fc = randcos(c)
    if fc*fa < 0:
      b = c
      fb = fc
    else:
      a = c
      fa = fc
    if b-a < xtol:
        #print('xtol reached, number of steps', i)
        return (a+b)/2
    #print('Maximum number of iterations reached')
  return (a+b)/2

bisectvalues = []

for i in range(10000):
    bisectvalues.append(bisect(randcos, 0, 4, 41, 10**(-12)))

print("first 100 entries in the list bisectvalues:\n", bisectvalues[:100], "\n")
bisect_std_dev = np.std(bisectvalues)

print("standard deviation for bisection: ", bisect_std_dev)

"""
def fixedpt(g, pzero, xtol, N):
    n = 1
    while n<N:
        print(n)
        pone = g(pzero)
        if np.abs(pone-pzero)<xtol:
            print('p is ', pone, ' and the iteration number is ', n)
            return
        pzero = pone
        n += 1
    print('Did not converge. The last estimate is p = ', pzero)

def fixed_point(g, x0, xtol=1e-6, max_iter=100, red_flags=2):
    
    Finds the fixed point of a function g using fixed-point iteration.

    Args:
        g: The function for which to find the fixed point.
        x0: The initial guess for the fixed point.
        tola: The desired absolute tolerance.
        max_iter: The maximum number of iterations to perform.
        red_flags: The number of consecutive failures to converge before raising an error.

    Output:
        A tuple containing the fixed point and the number of iterations performed.
    
    x = x0
    red_flag_count = 0
    dx_old = np.inf
    
    for i in range(max_iter):
        x_next = g(x)
        dx = abs(x_next - x)
        if dx < xtol:
            return x_next, i + 1
        if dx > dx_old:
            red_flag_count += 1
        else:
            red_flag_count = 0
        if red_flag_count >= red_flags:
            raise RuntimeError("Too many consecutive failures to converge.")
        dx_old = dx
        x = x_next
    raise RuntimeError("Failed to converge within maximum iterations.")
"""