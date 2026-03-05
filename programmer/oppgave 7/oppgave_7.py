import numpy as np
import matplotlib.pyplot as plt


a_gold = 127 # termisk diffusivitet for gull [mm^2/s]
a_air = 21 # termisk diffusivitet for luft [mm^2/s]
gold_nodes = 100 # antall noder i gull-laget
layer = 5 # antall lag med luft rundt gull-legemet
length = gold_nodes + 2*layer - 1 # fysisk dimesjon på systemet
nodes = length + 1 # størrelsen på systemet

alpha = np.ones((nodes, nodes)) * a_air # matrise for alpha verdier luft
alpha[layer:-layer, layer:-layer] = a_gold # fyller inn alpha verdier for gull

dx = length / (nodes-1) # delta x
dy = length / (nodes-1) # delta y

a_max = np.max(alpha) # Maksimal termisk diffusivitet
dt = min(dx**2 / (4 * a_max), dy**2 / (4 * a_max)) # delta tid

u = np.ones((nodes, nodes)) * 200 # initiell temperatur for luft
u[layer:-layer, layer:-layer] = 15 # initiell temperatur for gull

# Randbetingelser

u[0, :] = 200
u[-1, :] = 200

u[:, 0] = 200
u[:, -1] = 200

# Visualizing med plot

fig, axis = plt.subplots()

pcm = axis.pcolormesh(u, cmap=plt.cm.jet, vmin=0, vmax=200)
plt.colorbar(pcm, ax=axis)

axis.contour(alpha,
             levels=[(a_gold + a_air)/2],
             colors='black',
             linewidths=2)

# Simulering

counter = 0 

while u[55, 55] <= 60 : # Så lenge midtpunktet er under 60 grader 

    w = u.copy() # Lager ny matrise w, for å ikke endre på u i for løkkene

    for i in range(1, nodes - 1): # Itererer over x-retning
        for j in range(1, nodes - 1): # Itererer over y-retning

            dd_ux = (w[i-1, j] - 2*w[i, j] + w[i+1, j])/dx**2 # Senterdifferanse i x retning
            dd_uy = (w[i, j-1] - 2*w[i, j] + w[i, j+1])/dy**2 # Senterdifferanse i y retning

            u[i, j] = dt * alpha[i, j] * (dd_ux + dd_uy) + w[i, j] # Eulers fremover

    counter += dt 

    print(f"midtpunktet er {u[55, 55]:.3f} [C] ved {counter:.3f}[s]")

    # Oppdatering av plot

    pcm.set_array(u)
    axis.set_title("Distribution at t: {:.3f} [s].".format(counter))
    plt.pause(0.01)

plt.show()