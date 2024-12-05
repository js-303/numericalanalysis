import numpy as np
import matplotlib.pyplot as plt

monthly_kva = {}
yearly_kva = {}
month = []
b = []

with open("C:\\Users\Jamil Santos\Documents\math4650\homework\windmill.txt", "r") as file:
    lines = [int(line.rstrip()) for line in file]
file.close()
for i in range(len(lines)):
    monthly_kva[i+1] = lines[i]
    month.append((i+1)/12)
    b.append(lines[i])

t = np.array(month)
A = np.vstack([np.ones(len(t)),np.cos((2*np.pi)*t),np.sin((2*np.pi)*t),np.cos((4*np.pi)*t)]).T
b = np.array(b)
print(t)
print(b)

def least_squares_qr(A, b):
  m, n = A.shape
  Q = np.zeros((m, n))
  R = np.zeros((n, n))

  for j in range(n): 
    v = A[:, j]
    for i in range(j): 
      R[i, j] = np.dot(Q[:, i], v) 
      v = v - R[i, j] * Q[:, i]    
    R[j, j] = np.linalg.norm(v)
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

f = lambda t: QR[0]+QR[1]*np.cos(2*np.pi*t)+QR[2]*np.sin(2*np.pi*t)+QR[3]*np.cos(4*np.pi*t)
tt = np.linspace(0, 5, 1000)
ax = plt.axes()
plt.plot(tt, f(tt), label='periodic fit')
for i in range(len(b)):
   plt.plot(t[i], b[i], "o")
plt.title("Periodic fit of monthly MWh from JAN 2005 to DEC 2009")
plt.ylabel("MWh per month")
plt.xlabel("year t")
plt.legend()
plt.show()



