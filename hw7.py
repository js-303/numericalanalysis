import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp
from scipy.interpolate import CubicSpline
"""
x_points = [0,1,2,3]
y_points = [4,1,1,3]

def cubic_eval(breaks,coef,xx):
  yy = np.zeros(len(xx))
  breaks2 = np.concatenate(([np.min(xx)], breaks[1:-1], [np.max(xx)+1]))
  n = len(breaks) - 1
  for i in range(n):
    select = (xx>=breaks2[i]) & (xx<breaks2[i+1])
    nbr = np.sum(select)
    if nbr == 0:
      continue
    yy[select] = coef[i,3]*np.ones(nbr)
    for j in range(2,-1,-1):
      yy[select] = coef[i,j] + (xx[select]-breaks[i])*yy[select]
  return yy

xx = np.linspace(np.min(x_points),np.max(x_points),1001)
yy = cubic_eval(x_points,c2,xx)
plt.plot(x_points,y_points,'o',markersize=8)
plt.plot(xx,yy)
plt.show()


x_points = [0,1,2,3]
y_points = [3,5,4,1]
sp = CubicSpline(x_points, y_points, bc_type='not-a-knot')
print(sp.c)

A = np.array([[1,-2,1,0],
              [1,4,1,0],
              [0,1,4,1],
              [0,1,-2,1]])

b = np.array([[0],
              [-9],
              [-6],
              [0]])

c = np.linalg.solve(A,b).reshape(1,4)
print(c)

xx = np.linspace(np.min(x_points), np.max(x_points), 1000)
fig, ax = plt.subplots(figsize=(5,5))
ax.plot(x_points,y_points, 'o')
ax.plot(xx, sp(xx))
plt.show()

def findUB(a,b,n):
    ub = (((b-a)/2)**n)/(2**(n-1))
    return ub

print(findUB(-1,1,6))
"""
k = np.array([0, 4, 1, 5])
xk = np.sin(2*np.pi*k/3)
yk = np.cos(2*np.pi*k/3)
fig, ax = plt.subplots()
ax.plot(xk,yk,'o-',markersize=6)


t = np.arange(4)
#spx = interp.CubicSpline(t,xk)
#spy = interp.CubicSpline(t,yk)
spx = interp.CubicSpline(t,xk,bc_type='periodic')
spy = interp.CubicSpline(t,yk,bc_type='periodic')
tt = np.linspace(0,5,1001)
fig, ax = plt.subplots()
ax.plot(spx(tt),spy(tt),'-')
ax.set_aspect('equal')
plt.show()