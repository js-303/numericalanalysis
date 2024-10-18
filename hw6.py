import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import math

def interpN(x, y, xx):
  # calculate divided differences
  n = len(x)
  DD = y
  for m in range(1, n):
    for k in range(n-1,m-1,-1):
      DD[k] = (DD[k] - DD[k-1]) / (x[k] - x[k - m])

  # calculate polynomial
  yy = np.zeros(len(xx))
  for k in range(n-1,-1,-1):
    yy = DD[k] + (xx-x[k])*yy
  return yy

x_values = [1970, 1980, 1990, 2000, 2010, 2020]
y_values = [203.3, 226.5, 248.7, 281.4, 308.7, 331.4]

plt.plot(x_values,y_values,'o',markersize=10)
xx = np.linspace(min(x_values),max(x_values), 1000)
yy = interpN(x_values,y_values,xx)

p1 = np.polyfit(xx,yy, len(x_values)-1)
y = 275

find = lambda x: np.polyval(p1,x) - y
year = fsolve(find, 2000)
monthfrac, yearint = math.modf(year[0])
monthfl = monthfrac/(1/12)

months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUNE', 'JULY', 'AUG', 'SEPT', 'OCT', 'NOV', 'DEC']

print(monthfl)
if 0 <= monthfl < 12:
    month = months[int(monthfl)]
else:
    month = np.NaN
    print("invalid month value")

print("estimated US population in 1997: ", round(np.polyval(p1,1997), 1), "million")
print("predicted month when the US population reached 300 million: ", month,int(yearint))

plt.plot(1997, np.polyval(p1,1997), 'o', markersize=5, color='red')
plt.plot(year, y, 'o', markersize=5, color='purple')
plt.annotate((1997, round(np.polyval(p1,1997)),1), (1997, np.polyval(p1,1997)))
plt.annotate((str(month)+" "+str(int(yearint)), round(y,1)), (year, y))
plt.plot(xx, yy)
plt.show()
