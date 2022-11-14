n=int(input("n : "))
b = 0
for i in range(1,n+1):
    
    if n % i == 0:
             b +=1
if b == 2:


     print("primer")

else:
     print("ERORE")
