import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math as math

###

y0 = 0.480

A = 1.5554

tau = 13.264

def volt_to_cm(v):
    return(-tau*math.log((v-y0)/A))     # Fonction pour convertir les volts en cm, déterminée à partir de mesures préliminaires

mesures_volt = pd.read_excel ('Mesures positions.xlsx')     # On ouvre le tableur composé de toutes les mesures, en volt

mesures_volt = np.asarray(mesures_volt).T       # On convertit le tableau issu du package "panda" en tableau numpy

mesures_volt_coherent = []      # On créé un tableau cohérent où on élimine toutes les tensions inférieures à y0
                                # (ce qui n'est pas sensé arriver), cela correspond sans doute à un moment où
                                # le panneau réfléchissant s'est décalé de l'axe du capteur,
                                # le capteur se mettant donc à viser dans le vide, d'où les valeurs trop basses

for i in range(len(mesures_volt)):
    mesures_volt_coherent.append(mesures_volt[i][np.where(mesures_volt[i]>y0)])

mesures_distance = []       # Création d'un tableau de mesures de distance, où on convertit les volts en cm

distances_normalisees = []

for i in range(len(mesures_volt)):
    mesures_distance.append([volt_to_cm(v)/12.5 for v in mesures_volt_coherent[i]])

noms_mesures = ['Mesure 1-2','Mesure 1-3', 'Mesure 2-2', 'Mesure 2-3', 'Mesure 3-3']

subplots = [331,333,335,337,339]

for i in range(len(noms_mesures)):
    plt.subplot(subplots[i])
    plt.xlabel('Distance')
    plt.ylabel('Nombre de mesures')
    plt.hist(mesures_distance[i], bins = 20, density = True)
    plt.title(noms_mesures[i])
    plt.show()


### Modèle théorique 1 ( lattice gas model )

d = 4       # largeur du ring

l = 8       # longueur du ring

def P_stat(N):

    Omega_x = []
    Proba = []

    for x in range(l+1):      # x correspond à la distance de la paroie par rapport au capteur, on étudie toutes les positions possibles

        i = d*x         # surface du ring de gauche
        j = d*(8-x)     # surface du ring de droite

        OmegaG = math.comb(i,N[0])   # le nombre d'états(configurations) possibles a la gauche du systeme
        OmegaD = math.comb(j,N[1])   # le nombre d'états(configurations) possibles a la droite du systeme

        Omega_x.append(OmegaG * OmegaD)    # nombre total de configurations possible à un x donné

    Omega = sum(Omega_x)

    for i in range(l+1):

        Proba.append(Omega_x[i]/Omega)

    return(Proba)

x = [i for i in range(0,l+1)]

Config_Possibles = [[1, 2], [1, 3], [2, 2], [2, 3], [3, 3]]

for i in range(len(noms_mesures)):
    plt.subplot(subplots[i])
    plt.xlabel('Distance')
    plt.ylabel('Probabilité')
    plt.hist(mesures_distance[i], density = True, bins = 20)
    plt.plot(x, P_stat(Config_Possibles[i]))
    plt.title(noms_mesures[i])
    plt.show()












