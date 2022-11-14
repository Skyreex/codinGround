a = int(input("donner une valeur : "))
b= 0
for i in range (0,10):
    z = int(input(f"donner une valeur {i+1}: "))
    if z == a:
        b += 1

print(f"la première valeur a été saisie {b-1} fois ")
