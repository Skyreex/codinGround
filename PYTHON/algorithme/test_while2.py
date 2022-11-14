n = input("n : ")
pos, neg = 0, 0
""""""
if int(n) > 0:
    pos += 0
elif int(n) > 0:
    neg += 1
while n != 'N' and n != 'n':
    n = input("n : ")
    if n > '0':
        pos += 1
    elif n < '0':
        neg += 1

print(f"Nombres positive : {pos}\nNombres negative : {neg}")