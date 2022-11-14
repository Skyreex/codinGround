a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))
delta = int(b**2 - 4*a*c)
if delta>=0:
    x1 = float((-b + delta**(1/2)) / (2*a))
    print(x1)
    x2 = float((-b - delta**(1/2)) / (2*a))
    if x1 != x2:
        print(x2)
else: 
    print("pas de solution dans R")