taille = int(input("Veuillez entrer la taille du tableau : "))
tab = []
cube = []


def Remplissage_tab(T, val):
    for i in range(val):
        T.append(int(input(f"Entrez l'élement {i} : ")))


def si_cube(T, V):
    for i in T:
        for j in T:
            if i ** 3 == j:
                V.append(j)


Remplissage_tab(tab, taille)
si_cube(tab, cube)
print(f"les nombres qui ont leurs cube dans ce tableau sont :\n{cube}")
