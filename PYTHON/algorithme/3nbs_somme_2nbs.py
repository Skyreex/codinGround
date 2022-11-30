T = []
for i in range(0,3):
    T.append(int(input(f"entrez nombre {i+1} : ")))

T.sort()
if T[0] + T[1] == T[2]:
    print(T[2])
else:
    print("aucun nombre est la somme des autres")
