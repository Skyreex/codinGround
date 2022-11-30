a = int(input("a : "))
b = int(input("b : "))
if (a>0 and b>0) or (a<0 and b<0):
    print("Le produit est positif")
elif a == 0 or b == 0:
    print("Le produit est nulle")
else:
    print("Le produit est negatif")