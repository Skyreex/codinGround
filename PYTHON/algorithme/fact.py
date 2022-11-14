n = int(input("entrez n : "))
sum = 1
if n >= 0:
    for x in range(1, n):
        sum = sum + sum * x
else:
    for x in range(1, -n):
        sum = sum + sum * x
    sum *= -1
print(sum)
