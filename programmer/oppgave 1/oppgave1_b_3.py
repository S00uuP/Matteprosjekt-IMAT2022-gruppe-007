import numpy as np
import matplotlib.pyplot as plt

v_maks = 30
u_maks = 1
p = 2

u = np.linspace(0, u_maks, 500)

def v1(u):
    return v_maks * (np.cos(np.pi * u / (2 * u_maks)))**p

def v2(u):
    return v_maks * np.sqrt(1 - (u/u_maks)**p)

plt.figure()
plt.plot(u, v1(u))
plt.title("Modell 1")
plt.xlabel("u")
plt.ylabel("v(u)")
plt.ylim(bottom=0)
plt.show()


plt.figure()
plt.plot(u, v2(u))
plt.title("Modell 2")
plt.xlabel("u")
plt.ylabel("v(u)")
plt.ylim(bottom=0)
plt.show()


print("----- KRAVSJEKK MODELL 1 -----")
print("v(0) =", v1(0))
print("v(u_maks) =", v1(u_maks))
print("Min v =", np.min(v1(u)))
print("Max v =", np.max(v1(u)))

dv1 = np.gradient(v1(u), u)
print("Min dv/du =", np.min(dv1))

print("\n----- KRAVSJEKK MODELL 2 -----")
print("v(0) =", v2(0))
print("v(u_maks) =", v2(u_maks))
print("Min v =", np.min(v2(u)))
print("Max v =", np.max(v2(u)))

dv2 = np.gradient(v2(u), u)
print("Min dv/du =", np.min(dv2))
