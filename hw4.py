import numpy as np
import matplotlib.pyplot as plt


def meanerror(n):
    A = np.random.rand(n,n)
    x = np.random.rand(n)
    b = A.dot(x)
    y = np.linalg.solve(A,b)
    dx = np.mean(abs(x-y))
    return dx

test_n = [10,20,50,100,200,500,1000,2000]
#test_n = [2,3,4]

result = [[],[],[],[],[],[],[],[]]

for i in range(len(test_n)):
    result[i]=[]
    for j in range(1000):
        result[i].append(meanerror(test_n[i]))

mean_list = []
for i in range(len(result)):
    mean_list.append(np.mean(result[i]))
print(mean_list)

x = mean_list
y = test_n
fig, ax = plt.subplots()
ax.set_xlabel('mean error')
ax.set_ylabel('n-size')
plt.loglog(x,y)
plt.show()
