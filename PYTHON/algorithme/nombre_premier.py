n = int(input("n : "))
for i in range (2,n+1):
    b=0
    for j in range (1,n+1):
        if i%j == 0:
            b+=1
    if b==2:
        print(i)
