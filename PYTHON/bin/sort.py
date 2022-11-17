T = [41,5,88,4,3,39]
taille = len(T)

for i in range (0,taille):
    min = T[i]
    position = i
    for j in range(i+1,taille):
        if T[j] > min:
            min = T[j]
            position = j

    for k in range(position,i-1,-1):
        T[k] = T[k-1]

print(T)
