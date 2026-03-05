import numpy as np
import matplotlib.pyplot as plt

v_maks = 30
x_min = -1000
x_maks = 1000

x = np.linspace(x_min, x_maks, 2000)

def u0(x):
    return np.where(x < 0, 1, 0)

plt.figure()
plt.plot(x, u0(x))
plt.xlabel("x")
plt.ylabel("u(x)")
plt.grid(True)
plt.show()
