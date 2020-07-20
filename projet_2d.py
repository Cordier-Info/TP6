# Méthode pour lire un fichier en binaire et récupérer le résultat sous la forme d'un chaîne de caractères constituée de '1' et de '0' :

f = open('imageNB_comp.dat','rb')
code_bytes = f.read()
f.close()
code_texte = ''
for b in code_bytes :
    code_texte += format(b,'08b') # on obtient le texte codé (avec seulement des 1 et des 0)
