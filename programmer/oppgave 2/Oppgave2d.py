import numpy as np
import matplotlib.pyplot as plt

vmax = 8.33          # m/s (~54 km/h)
umax = 0.213         # biler per meter 

# diskretisering
x_min, x_max = -1000, 1000
Nx = 800
x = np.linspace(x_min, x_max, Nx)
dx = x[1] - x[0]

p_verdi = 5
# Tidsdiskretisering
T = 400               # sekunder
dt = 0.05
Nt = int(T/dt)

# Initialbetingelse
u0 = np.zeros(Nx)
u0[x < 0] = umax

def simulerbil(U, p_verdi):
    def v(u_local):
        return vmax * (1 - (u_local/umax)**p_verdi)
    
    P = np.zeros(Nt)
    V = np.zeros(Nt)
    P[0] = -1000
    V[0] = 0
    
    for n in range(1, Nt):
        u_point = np.interp(P[n-1], x, U[n-1])   # U[n-1] er nå 1D array over x
        V[n] = v(u_point)
        P[n] = P[n-1] + V[n-1]*dt
    return P, V
def solve_for_p(p_verdi):
    u = u0.copy()
    
    def flux(u):
        return vmax * (u - (u**(p_verdi+1)) / (umax**p_verdi))
    
    # lagre tidsrekke: Nt x Nx
    U = np.zeros((Nt, Nx))
    U[0] = u.copy()
    
    for n in range(1, Nt):
        F = flux(u)
        u_new = u.copy()
        
        # Lax-Friedrichs oppdatering
        u_new[1:-1] = (
            0.5 * (u[2:] + u[:-2])
            - (dt/(2*dx)) * (F[2:] - F[:-2])
        )
        
        # Randbetingelser
        u_new[0] = umax
        u_new[0] = 0.0
        
        u = u_new
        U[n] = u.copy()
    
    return U
U = solve_for_p(p_verdi)
P, V = simulerbil(U, p_verdi)
plt.figure()
plt.plot(np.linspace(0, T, Nt), P, label='Posisjon')
plt.xlabel('Tid (s)')
plt.ylabel('Posisjon (m)')
plt.title(f'Posisjon av bil over tid, p={p_verdi}')
plt.grid()
plt.show()

plt.figure()
plt.plot(np.linspace(0, T, Nt), V, label='Fart')
plt.xlabel('Tid (s)')
plt.ylabel('Fart (m/s)')
plt.title(f'Fart til bil over tid, p={p_verdi}')
plt.grid()
plt.show()