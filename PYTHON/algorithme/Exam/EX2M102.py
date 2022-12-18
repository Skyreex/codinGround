val = int(input("Veuillez entrer une valeur : "))


def nb_premier(n):
    T = []
    for i in range(1, n + 1):
        temp = 0
        for j in range(1, n + 1):
            if i % j == 0:
                temp += 1
        if temp == 2:
            T.append(i)
    return T


def carrée(tab):
    for i in tab:
        print(f"{i ** 2} carrée de {i}")


carrée(nb_premier(val))
