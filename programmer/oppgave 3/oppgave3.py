import numpy as np
import matplotlib.pyplot as plt

N = 100
h = 2 / N

x = np.linspace(-1, 1, N+1)
n = N - 1

A = np.zeros((n, n))

for i in range(n):
    A[i, i] = -2
    if i > 0:
        A[i, i-1] = 1
    if i < n-1:
        A[i, i+1] = 1

A = A / h**2

b = np.cos(np.pi * x[1:N])

b[0] -= 0 / h**2      # u(-1)=0
b[-1] -= 2 / h**2     # u(1)=2

u_inner = np.linalg.solve(A, b)

u = np.zeros(N+1)
u[0] = 0
u[-1] = 2
u[1:N] = u_inner

u_exact = x + 1 - (1/np.pi**2)*(np.cos(np.pi*x) + 1)

plt.plot(x, u, label="Numerisk")
plt.plot(x, u_exact, '--', label="Analytisk")
plt.legend()
plt.show()
