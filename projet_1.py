# le corps du code ne doit pas être touché
# par contre, vous devez comprendre le rôle et écrire les différentes fonctions utilisées 
nim = initialise()
affiche(nim)
while sum(nim) != 0 :
    ns = nim_somme(nim)
    if ns == 0 :
        nim = tour_humain(nim)
    else :
        nim = tour_machine(nim,ns)
    affiche(nim)
print("Vous avez perdu...\n")
