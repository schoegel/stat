import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math as math

y0 = 0.480

A = 1.5554

tau = 13.264

def volt_to_cm(v):
    return(v - y0)

mesures_volt = pd.read_excel ('Mesures positions.xlsx')

mesures_volt = np.asarray(mesures_volt).T

mesures_volt_coherent = []

for i in range(len(mesures_volt)):
    mesures_volt_coherent.append(mesures_volt[i][np.where(mesures_volt[i]>y0)])

mesures_distance = []

for i in range(len(mesures_volt)):
    mesures_distance.append([volt_to_cm(x) for x in mesures_volt[i]])

noms_mesures = ['Mesure 1-2','Mesure 1-3', 'Mesure 2-2', 'Mesure 2-3', 'Mesure 3-3']
subplots = [331,333,335,337,339]

for i in range(len(noms_mesures)):
    plt.subplot(subplots[i])
    plt.xlabel('Distance')
    plt.ylabel('Nombre de mesures')
    plt.hist(mesures_distance[i], bins = 20)
    plt.title(noms_mesures[i])
    plt.show()


### modèle théorique 1 ( lattice gas model )

# Nb =  # nombre de point

Ng = 2 #nombre de boules à gauche

Nd = 1 #nombre de boules à droite

d = 4 #largeur du ring

l = 8 #longueur du ring

x = 0 #distance capteur - barre

i = d*x #surface du premier ring (g)

j = d*(8-x) #taillle du second ring (d)

OmegaG = math.comb(i*j,Ng)    #le nombre d'états(configurations) possible a la gauche du systeme

OmegaD = math.comb(i*j,Nd)   #le nombre d'états(configurations) possible a la droite du systeme

Omega = OmegaG * OmegaD       #nombre total de configurations possible dans l'ensemble du systeme

ar = math.isqrt(Gammatot/Gammar)         #Air total de déplacement des boules en fonction du nombre des autres boules dans le même ring (droite)

al = math.isqrt(Gammatot/Gammal)

A = 68*34                     #Air total de déplacement des boules en fonction du nombre des autres boules dans le même ring (droite)

### Donnée

Nb = input("la valeur de Nb")

Nl = input("la valeur de Nl")

Ng = input("la valeur de Ng")

x =  input("position du barrau")

###right or left

###valeur théorique ( lattice gas model )


For i in range(Nb) :
    x =  input("position du barreau")
    for j in range(Nl) :
        lgml = al**2*(A/al)((A/al)-1)
    for w in range(Ng):
        lgmr = ar**2*(A/ar)((A/ar)-1)


lgm = a**2*(A/a)((A/a)-1)



















