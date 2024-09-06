import numpy as np
import matplotlib.pyplot as plt

f = lambda x: 1-np.cos(x)
g = lambda x: (np.sin(x)**2)/(1+np.cos(x))

x_values = [0.1, 0.01, 0.001, 10**(-4), 10**(-5), 10**(-6), 10**(-7)]
f_values = []
g_values = []
re_values = []
ae_values = []

for i in range(len(x_values)):
    f_values.append(f(x_values[i]))
    g_values.append(g(x_values[i]))
    re_values.append(abs(f_values[i]-g_values[i])/abs(f_values[i]))
    ae_values.append(abs(f_values[i]-g_values[i]))
print(f_values)
print(g_values)
print(re_values)
print(ae_values)


plt.figure(figsize=(10, 6))
plt.plot(x_values, f(x_values), label='f', color ='green')
plt.plot(x_values, g(x_values), label='g', color ='red', linestyle='dashed')

plt.grid(True)
plt.show()