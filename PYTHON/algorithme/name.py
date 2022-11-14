a = input("enter a name : ")
b = input("enter a name : ")
for i in range(0, len(a)):
    if a[i]>b[i]:
        print(b)
        break
    elif a[i]<b[i]:
        print(a)
        break
    elif a==b:
        print(a)
        break
