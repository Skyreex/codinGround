"""
n = int(input("n : "))
pair,impair = 0,0
pair2,impair2 = 1,1

for i in range (1,n+1):
    if i % 2 == 0:
        pair = pair + i
        pair2 = pair2*i
    else:
        impair = impair + i
        impair2 = impair2 * i

print(f"SOMME - \"pair : {pair} // impair : {impair}\"")
print(f"PRODUIT - \"pair : {pair2} // impair : {impair2}\"")
"""
n=int(input("n : "))
pair,impair=0,0
for i in range(1,n+1):
    if i % 2 == 0:
       pair = pair+i
       print(f"pair {i}")
    else:
        pair = pair + i
        print(f"impair {i}")