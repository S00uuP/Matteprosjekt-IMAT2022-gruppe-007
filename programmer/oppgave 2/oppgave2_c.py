import numpy as np
import matplotlib.pyplot as plt
# Fysiske parametere
vmax = 8.33          # m/s (54 km/h)
umax = 0.213          # biler per meter (1 bil per 6-7 meter)

#diskretisering
x_min, x_max = -1000, 1000
Nx = 800
x = np.linspace(x_min, x_max, Nx)
dx = x[1] - x[0]

# Tidsdiskretisering
T = 120              # sekunder
dt = 0.05
Nt = int(T/dt)

# Initialbetingelse
# Kø bak lyset (x<0)
u0 = np.zeros(Nx)
u0[x < 0] = umax

# Løser for gitt p-verdi
def solve_for_p(p_value):
    u = u0.copy()
    
    def flux(u):
        return vmax * (u - (u**(p_value+1)) / (umax**p_value))
    
    for n in range(Nt):
        F = flux(u)
        u_new = u.copy()
        
        # Lax-Friedrichs oppdatering
        u_new[1:-1] = (
            0.5 * (u[2:] + u[:-2])
            - (dt/(2*dx)) * (F[2:] - F[:-2])
        )
        
        # Randbetingelser
        u_new[0] = 0      # det kommer ingen biler inn fra venstre
        u_new[-1] = 0.0      # u(1000,t) = 0
        
        u = u_new
    
    return u

#plotter for de ulike p verdiene
for p_value in [1, 2, 5]:
    u_final = solve_for_p(p_value)
    
    plt.figure()
    plt.plot(x, u_final)
    plt.xlabel("x (m)")
    plt.ylabel("u(x,t)")
    plt.title(f"Lax-Friedrichs løsning etter {T}s, p = {p_value}")
    plt.ylim(-0.01, umax + 0.02)
    plt.show()import matplotlib.animation as an
import matplotlib.pyplot as plt
import numpy as np

