import numpy as np
import matplotlib.pyplot as plt

u_maks = 1
v_maks = 30
p_values = np.arange(1, 11)

u = np.linspace(0, u_maks, 500)

def v1(u, p):
    return v_maks * (1 - (u/u_maks)**p)

def v2(u, p):
    return u * v_maks * (1 - (u/u_maks)**p)

#plot til i
plt.figure()
for p in p_values:
    plt.plot(u, v1(u, p), label=f"Fart, p = {p}")
plt.legend()
plt.xlabel("u")
plt.ylabel("v(u)")
plt.grid(True)
#plt.show()

plt.figure()
for p in p_values:
    plt.plot(u, v2(u, p), label=f"Flux, p = {p}")
plt.legend()
plt.xlabel("u")
plt.ylabel("j(u)")
plt.grid(True)
#plt.show()

plt.figure()
plt.plot(u, v1(u, 1), label="Fart, p = 1")
plt.plot(u, v2(u, 1), label="Flux, p = 1")
u_topp = u_maks/2
v_topp = v2(u_topp, 1)
plt.scatter(u_topp, v_topp)
plt.annotate("Høyeste flux",
             (u_topp, v_topp),
             textcoords="offset points",
             xytext=(0,-20))
plt.legend()
plt.xlabel("u")
plt.ylabel("j(u)/v(u)")
plt.grid(True)
plt.show()