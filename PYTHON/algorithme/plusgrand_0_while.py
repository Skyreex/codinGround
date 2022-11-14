n = int(input("n : "))
max = n
p , p_max = 1,1

while n!=0:
    n = int(input("n : "))
    p += 1
    if n > max:
        max = n
        p_max = p

print(f"n = {max} position = {p_max}")