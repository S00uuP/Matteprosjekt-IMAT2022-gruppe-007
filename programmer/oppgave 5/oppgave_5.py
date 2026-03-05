# Importerer nødvendige biblioteker
import numpy as np
import matplotlib.pyplot as plt

# Definerer parametere for gridet
Nx = 50
Ny = 20
ax, bx = -5, 5
ay, by = 0, 2

hx = (bx - ax) / Nx # Finner steglengde for x
hy = (by - ay) / Ny # Finner steglengde for Y

x = np.linspace(ax, bx, Nx+1) # Lager alle punktene i gridet
y = np.linspace(ay, by, Ny+1) # 51 punkter i X og 21 punkter i Y

N = (Nx - 1)*(Ny - 1) # Finner antall ukjente 
A = np.zeros((N,N)) # Lager matrise for koeffisienten
rhs = np.zeros(N) # Lager høyresidevektor

# Definerer funksjon for å finne indeks i ukjent vektor
def idx(i, j): 
    return i + (Nx - 1) * j

# Finner koeffisientene i A
# Se forklaring i tekst
for j in range(Ny - 1): 
    for i in range(Nx - 1):
        k = idx(i, j)
        A[k, k] = -4 
        if i > 0:
            A[k, idx(i-1, j)] = 1
        else:
            rhs[k] -= np.sin(2 * np.pi*y[j+1])
        if i < Nx - 2:
            A[k, idx(i+1, j)] = 1
        else:
            rhs[k] -= np.sin(2 * np.pi*y[j+1])
        if j > 0:
            A[k, idx(i, j -1)] = 1
        else:
            rhs[k] -= 0
        if j < Ny - 2:
            A[k, idx(i, j+1)] = 1
        else:
            rhs[k] -= np.sin(np.pi * x[i+1])

u_inner = np.linalg.solve(A, rhs) # Løser det lineære systemet
u = np.zeros((Nx + 1, Ny + 1)) # Lager matrise med løsninger

# Definerer randbetingelser
u[0,:] = np.sin(2 * np.pi * y)
u[-1,:] = np.sin(2 * np.pi * y)
u[:,0] = 0
u[:,-1] = np.sin(np.pi * x)

# Fyller inn løsninger i u
for j in range (Ny - 1):
    for i in range (Nx - 1):
        u[i + 1, j + 1] = u_inner[idx(i, j)]

# Lager koordinater for plotting
X,Y = np.meshgrid(x,y,indexing='ij')

# Plotter løsningene
plt.figure()
plt.contourf(X, Y, u, 20)
plt.colorbar()
plt.show()
