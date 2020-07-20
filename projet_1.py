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
