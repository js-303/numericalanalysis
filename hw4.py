import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def meanerror(n):
    A = np.random.rand(n,n)
    x = np.random.rand(n)
    b = A.dot(x)
    y = np.linalg.solve(A,b)
    dx = np.mean(abs(x-y))
    print(x,y,dx)
    return dx
meanerror(5)
"""
#test_n = [10,20,50,100,200,500,1000,2000]
test_n = [2,5,50,100, 200]

result = [[],[],[],[],[],[],[],[]]
running_list = [[],[],[],[],[],[],[],[]]

for i in range(len(test_n)):
    result[i]=[]
    index = []
    total = 0
    for j in range(1000):
        result[i].append(meanerror(test_n[i]))
        index.append(j+1)
    for k in range(len(index)):
        total += result[i][k]
        running_list[i].append(total/(k+1))
        #print(running_list[i][k], index[k]   
"""



"""
for i in range(len(index)):
    x = running_list[i]
    y = index

    fig, ax = plt.subplots()
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_adjustable("datalim")
    ax.scatter(x,y)

    ax.set_xlabel('average mean error')
    ax.set_ylabel('number of iterations')


    plt.show()
"""
