import numpy as np
import matplotlib.pyplot as plt

Nx = 100
Ny = 100

x = np.linspace(0, 100, Nx + 1)
y = np.linspace(0, 100, Ny + 1)

dx = x[1] - x[0]
dy = y[1] - y[0]

x_in = x[1:-1]
y_in = y[1:-1]

# use interior sizes
nx = Nx - 1
ny = Ny - 1

# build 1D Laplacians for interior nodes (size nx x nx and ny x ny)
Lx = (1 / dx**2) * (
    np.diag(np.ones(nx - 1), -1) +
    np.diag(-2 * np.ones(nx), 0) +
    np.diag(np.ones(nx - 1), 1)
)
Ix = np.eye(nx)

Ly = (1 / dy**2) * (
    np.diag(np.ones(ny - 1), -1) +
    np.diag(-2 * np.ones(ny), 0) +
    np.diag(np.ones(ny - 1), 1)
)
Iy = np.eye(ny)

L = np.kron(Lx, Iy) + np.kron(Ix, Ly)

# Dirichlet boundary functions (return arrays matching input coordinate arrays)
def b(x):
    return 200 * np.ones_like(x)   # bottom (y=0)

def t(x):
    return 200 * np.ones_like(x)   # top (y=100)

def v(y):
    return 200 * np.ones_like(y)   # left (x=0)

def h(y):
    return 200 * np.ones_like(y)   # right (x=100)

# assemble boundary contribution vector F (size nx*ny)
F = np.zeros(nx * ny)

# bottom and top boundaries: vary with x_in, affect j=0 and j=ny-1 (y-direction neighbors)
B = b(x_in)  # length nx
T = t(x_in)  # length nx

# left and right boundaries: vary with y_in, affect i=0 and i=nx-1 (x-direction neighbors)
V = v(y_in)  # length ny
H = h(y_in)  # length ny

# add contributions: for node (i,j) flattened index = i*ny + j (row-major)
for i in range(nx):
    for j in range(ny):
        idx = i * ny + j
        # neighbor below (j-1) is boundary when j==0 => add B[i]/dy^2
        if j == 0:
            F[idx] += B[i] / dy**2
        # neighbor above (j+1) is boundary when j==ny-1 => add T[i]/dy^2
        if j == ny - 1:
            F[idx] += T[i] / dy**2
        # neighbor left (i-1) is boundary when i==0 => add V[j]/dx**2
        if i == 0:
            F[idx] += V[j] / dx**2
        # neighbor right (i+1) is boundary when i==nx-1 => add H[j]/dx**2
        if i == nx - 1:
            F[idx] += H[j] / dx**2

def euler (g, u0, t0, t1, M):
    t = np.linspace(t0, t1, M)
    dt = t[1] - t[0]
    u = np.zeros((M, u0.size))
    u[0, :] = u0
    for i in range(M - 1):
        u[i + 1, :] = u[i, :] + dt * g(u[i, :], t[i])
    return u, t

def g(u, t):
    # Laplacian on interior plus boundary contribution
    return L @ u + F

X, Y = np.meshgrid(x_in, y_in, indexing='ij')

U0 = Y
num_unknowns = nx * ny
u0 = np.reshape(U0, num_unknowns)

u, t = euler(g, u0, 0, 60, 1000)

step = 500

Z = np.reshape(u[step, :], (nx, ny))
    
fig, ax = plt.subplots(
    subplot_kw = {"projection": "3d"},
    figsize = (10, 8)
)

ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlim(x_in[0], x_in[-1])
ax.set_ylim(y_in[0], y_in[-1])
ax.set_zlim(np.min(Z), np.max(Z))

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('u(x, y, t)')
ax.set_title(f'Temperaturfordeling ved t={t[step]:.2f} s')

plt.show()