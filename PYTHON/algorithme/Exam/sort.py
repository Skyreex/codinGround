tab = [0, 54, 1, 34, 22, 4, 23, 25, 13, 1, 23]
v = len(tab) - 1
print(tab)
exitloop = False
while not exitloop:
    exitloop = True
    for i in range(0, v):
        if tab[i] > tab[i + 1]:
            tab[i], tab[i + 1] = tab[i + 1], tab[i]
            exitloop = False

print(tab)
