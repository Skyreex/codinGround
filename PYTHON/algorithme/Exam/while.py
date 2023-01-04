liste = [1, 2, 3, 4, 5, 6]
# 1
print(len(liste))
# 2
print(liste[2])
# 3
print(liste[2:5])  # [3, 4, 5]


# 4
def somme(l):
    sum = 0
    for i in l:
        sum += i
    return sum


print(somme(liste))
# 5
print(liste[0:5:2])
# 6
print(liste)