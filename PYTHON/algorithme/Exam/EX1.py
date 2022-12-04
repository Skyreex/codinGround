nombres = []
somme = 0
taille = int(input("Entrez le nombre de valeur a saisir : "))

for i in range(0, taille):
    nombres.append(int(input("N : ")))
    somme = somme + nombres[i]

PG = max(nombres)
PP = min(nombres)

print(f"Le plus petit nombres est {PP} sa valeur carrée est {pow(PP,2)}")
print(f"Le plus petit nombres est {PG} sa valeur carrée est {pow(PG,2)}")
print(f"La moyenne de touts ces nombres est {somme/taille}")
