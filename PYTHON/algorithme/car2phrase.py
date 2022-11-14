a = input("Entrez a : ")
e = a

while a != '.':
    a = input("Entrez a : ")
    if a == '0':
        a = ' '
    e = e + a

print(e[:-1])

