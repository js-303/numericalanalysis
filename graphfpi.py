import numpy as np
from matplotlib.pyplot import figure, plot, title, legend, grid, show
import math

g = lambda x: 2*x**3-5*x-1
a = -10
b = 10
x = np.linspace(a, b)
n = int(input("input n value: "))
x_i = float(input("input initial value: "))
figure(figsize=(8,8))
plot(x, x, "g")
plot(x, g(x), "r")
grid(True)

for i in range(n):
    g_x_i = g(x_i)
    plot([x_i, x_i], [x_i, g(x_i)], "b")
    x_i_plus_1 = g(x_i)
    plot([x_i, g(x_i)], [x_i_plus_1, x_i_plus_1], "b")
    x_i = x_i_plus_1
    print(f"x_{i+1} = {x_i_plus_1}")
show()

