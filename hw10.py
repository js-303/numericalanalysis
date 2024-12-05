import numpy as np
import matplotlib.pyplot as plt

i=0
monthly_kva = {}
yearly_kva = {}

with open("C:\\Users\jamil\Documents\MATH4650\homework\windmill.txt", "r") as file:
    lines = [int(line.rstrip()) for line in file]
file.close()
for i in range(len(lines)):
    monthly_kva[i+1] = lines[i]
def yearly(dict):
    values = list(dict.values())
    result = []
    for i in range(0, len(values), 12):
        result.append(sum(values[i:i+12]))
    return result
for i in range(len(yearly(monthly_kva))):
    yearly_kva[i+1] = yearly(monthly_kva)[i]



t = np.array([0, 1, 2, 3, 4, 5])
A = np.vstack([np.ones(len(t)),np.cos(2*np.pi*t),np.sin(2*np.pi*t),np.cos(4*np.pi*t)]).T
b = np.array([0,2726,2772,2912,2702,2682])
print(A)

def least_squares_qr(A, b):
  m, n = A.shape
  Q = np.zeros((m, n))
  R = np.zeros((n, n))

  for j in range(n): # working with column j
    v = A[:, j]
    for i in range(j): # all columns i before j are already orthonormal
      R[i, j] = np.dot(Q[:, i], v) # project column j on column i
      v = v - R[i, j] * Q[:, i]    # find part of column j orthogonal to column i

    R[j, j] = np.linalg.norm(v) #normalize column j
    Q[:, j] = v / R[j, j]
  Qb = np.dot(Q.T, b)
  x = np.zeros(n)
  for i in range(n - 1, -1, -1):
    x[i] = Qb[i]
    for j in range(i+1,n):
      x[i] -= R[i,j]*x[j]
    x[i] /= R[i, i]

  return x
QR = least_squares_qr(A,b)
print(QR)

f = lambda t: QR[3]+QR[2]*np.cos(2*np.pi*t)+QR[1]*np.sin(2*np.pi*t)+QR[0]*np.cos(4*np.pi*t)
tt = np.linspace(0, 5, 1000)
plt.plot(tt, f(tt))
plt.show()