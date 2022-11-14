n = int(input("n : "))
p = 0
sum = n

while n!=0:
    p += 1
    n = int(input("n : "))
    sum = sum + n

print(f"moyenne = {sum/p}")