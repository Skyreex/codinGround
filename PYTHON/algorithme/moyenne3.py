
"""
def matiere(note, coeff):
    return note * coeff

mat = ["math","francais","PC","anglais","HG"]
coeffs, sum = 0, 0
for j in range(1,26):
    print(f"l'etudiant {j}")
    sum = 0
    for i in range(0, len(mat)):
        note = float(input(f"entrez la note de {mat[i]} : "))
        coeff = int(input(f"entrez le coefficient de {mat[i]} : "))
        noteT = [i]
        coeffs = coeffs + coeff
        finalnote = matiere(noteT[i], coeff)
        sum = sum + finalnote

    print(f"La moyenne génerale est : {sum / coeffs}")

"""
mat = ["math","francais","PC","anglais","HG"]
for j in range(1,26):
    print(f"l'etudiant {j}")
    sum = 0
    for i in range(0, len(mat)):
        note = float(input(f"entrez la note de {mat[i]} : "))
        noteT = [i]
        sum = sum

    print(f"La moyenne génerale est : {sum}")
