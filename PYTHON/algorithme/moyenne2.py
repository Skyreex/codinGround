def matiere(a, b):
    return a * b


coeffs, sum = 0, 0
j = int(input("nb de matieres : "))
for i in range(0, j):
    mat = input("entrez la matiére : ")
    note = float(input(f"entrez la note de {mat} : "))
    coeff = int(input(f"entrez le coefficient de {mat} : "))
    coeffs = coeffs + coeff
    finalnote = matiere(note, coeff)
    sum = sum + finalnote

print(f"La moyenne génerale est : {sum / coeffs}")
