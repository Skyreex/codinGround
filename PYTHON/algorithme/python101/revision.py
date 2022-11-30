"""
print(chr(93))
# a
print(ord('z'))
# 122
print(chr(65))
# A
print(ord('Z'))
# 90
tab = [3, 8, 54,5]
tab.sort(reverse=True)
print(tab)

z = 65+1j
print(type(z))
print(int('100', 2))
"""


"""
a = int(input("a : "))
somme = 0
for i in range (0, a+1, 1):
    somme = i + somme

    # i = 0    somme = 0
    # i = 1    somme = 1
    # i = 2    somme = 3
    # i = 3    somme = 6
    # i = 4    somme = 10
    # i = 5    somme = 15

print(f"la somme est : {somme}")

"""

"""
N = int(input("N : "))
val = 1

for i in range(2,N+1):
    val = val * i

print(f"fact de {N} est {val}")


"""
"""
a = 5
b = 4
print(a , "+" , b, "=" , a+b )
print("{} + {} = {}".format(a, b ,a+b))
print(f"{a} + {b} = {a+b}")



N = int(input("N : "))
for i in range (1,11):
    print(f"{N} * {i} = {N*i}")
"""

"""
max = 0
for i in range(1,7):
    a = int(input(f"Entrez le nombre numéro {i} : "))
    if a > max:
        max = a
        pos = i

print(f"Le plus grand de ces nombres est : {max} \nSa position est : {pos}")

"""

"""

max = 0
i = 1
while i < 7:
    a = int(input(f"Entrez le nombre numéro {i} : "))
    if a > max:
        max = a
        pos = i
    i += 1 # i+=1 <=> i = i + 1

print(f"Le plus grand de ces nombres est : {max} \nSa position est : {pos}")
"""

"""

mdp = input("Entrez le mdp : ")
while mdp != "admin":
    if mdp == "admin":
        print("connexion réussie")
    else:
        print("connexion échouée")
        mdp = input("Entrez le mdp : ")
"""

