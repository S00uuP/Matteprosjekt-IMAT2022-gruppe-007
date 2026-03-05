import numpy as np
import matplotlib.pyplot as plt

# Antall intervaller
N = 100
h = 2 / N

# Romgitter
x = np.linspace(-1, 1, N+1)

# Antall indre punkter
n = N - 1

# Lag matrise A
A = np.zeros((n, n))

for i in range(n):
    A[i, i] = -2
    if i > 0:
        A[i, i-1] = 1
    if i < n-1:
        A[i, i+1] = 1

A = A / h**2

# Høyreside
b = np.cos(np.pi * x[1:N])

# Juster for randbetingelser
b[0] -= 0 / h**2      # u(-1)=0
b[-1] -= 2 / h**2     # u(1)=2

# Løs systemet
u_inner = np.linalg.solve(A, b)

# Sett sammen full løsning
u = np.zeros(N+1)
u[0] = 0
u[-1] = 2
u[1:N] = u_inner

# Plot
plt.plot(x, u, label="Numerisk løsning")
plt.xlabel("x")
plt.ylabel("u(x)")
plt.title("Numerisk løsning av u'' = cos(pi x)")
plt.legend()
plt.grid()
plt.show()

u_exact = x + 1 - (1/np.pi**2)*(np.cos(np.pi*x) + 1)

plt.plot(x, u, label="Numerisk")
plt.plot(x, u_exact, '--', label="Analytisk")
plt.legend()
plt.show()
