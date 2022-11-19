def fact(sum,i):
    return sum * i

n = int(input("N : "))
sum = n
if n!=0:
    for i in range(n-1, 1,-1):
        sum = fact(sum,i)
else:
    sum = 1
print(sum)
