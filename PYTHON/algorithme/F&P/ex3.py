def Inverse(a):
    return 1/a

y = int(input("Entrez y : "))
while y == 0:
    y = int(input("Entrez y : "))

print("{} est l'inverse de {}".format(Inverse(y),y))
