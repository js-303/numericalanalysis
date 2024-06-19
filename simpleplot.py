import numpy as np
import math
import matplotlib.pyplot as mp

f = lambda x: math.cos(x)-math.sin(x)

x = np.linspace(-20,20)
y = f(x)


mp.plot(x, y)
mp.grid()
mp.show()