nombres = [0,0,0,0,0,0]

for i in range (0,7):
    nombres[i] = int(input(f"Entrez le nombre numéro {i+1} : "))

print(f"Le plus grand de ces nombres est : {max(nombres)}")