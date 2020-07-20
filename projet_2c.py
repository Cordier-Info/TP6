# méthode pour écrire un fichier en binaire :

f = open('imageNB_comp.dat','wb')
# s : chaîne de caractères obtenue en remplaçant chaque caractère
# du fichier original par son code issu de l'arbre
s = '1001110011...' 
# b est la transcription de ce code en bytes
b = bytes(int(s[i : i + 8], 2) for i in range(0, len(s), 8))
# puis on l'écrit dans f
f.write(b)
f.close()
