a = int(input("a : "))
while a > 10 or a < 0:
    a = int(input("a : "))
for i in range(1, 11):
    print(f"{a} * {i} = {a * i}")
