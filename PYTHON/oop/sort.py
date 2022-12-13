T = [3, 43, 6, 674, 7, 99, 2]
V = []
name = input("name : ")
V.extend(name)


def sort1(Tab):
    Tab.sort()


def sort2(Tab):
    Tab.sort()
    phrase = ""
    for i in Tab:
        phrase += i
    return phrase


sort1(T)
print(sort2(V))

print(T)
print(V)
