import math

# Initialisation des variables
Force = 10000  # en N
Module_young = 210  # en GPa = 10^3 N/mm^2
Longueur = 100  # en mm

# poutre rectangulaire
largeur_rect = 10  # en mm
longueur_rect = 20  # en mm

# poutre carrée
cote = 15  # en mm

# poutre ronde
diametre = 5  # en mm

# poutre creuse
Grand_diametre = 15  # en mm
Petit_diametre = 5  # en mm


# Calcul de la section optimale
Irect = (largeur_rect*(longueur_rect**3))/12
delta_maxrect = float(Force*(Longueur**3)/(3*Module_young*Irect))
Icar = (cote**4)/12
delta_maxcar = float(Force*(Longueur**3)/(3*Module_young*Icar))
Iron = (math.pi*(diametre**4))/64
delta_maxron = float(Force*(Longueur**3)/(3*Module_young*Iron))
Icreu = (math.pi*(Grand_diametre**4)-(Petit_diametre**4))/64
delta_maxcreu = float(Force*(Longueur**3)/(3*Module_young*Icreu))

def section_optimale(delta_maxrect,delta_maxcar,delta_maxron,delta_maxcreu) :
    delta_max= delta_maxrect
    if delta_maxcar < delta_max :
        delta_max= delta_maxcar
    if delta_maxron < delta_max :
        delta_max= delta_maxron
    if delta_maxcreu < delta_max :
        delta_max= delta_maxcreu
    return delta_max


deltasecoptimale = section_optimale(delta_maxrect,delta_maxcar,delta_maxron,delta_maxcreu)
if deltasecoptimale == delta_maxrect :
    print('Le type de section minimisant la déformation maximale est rectangle, avec une déformation de', round(delta_maxrect,2) ,'mm')
elif deltasecoptimale == delta_maxcar :
    print('Le type de section minimisant la déformation maximale est carrée, avec une déformation de ',round(delta_maxcar,2), 'mm')
elif deltasecoptimale == delta_maxron :
    print('Le type de section minimisant la déformation maximale est ronde, avec une déformation de ',round(delta_maxron,2) ,'mm')
elif deltasecoptimale == delta_maxcreu :
    print('Le type de section minimisant la déformation maximale est creuse, avec une déformation de' ,round(delta_maxcreu,2) ,'mm')
