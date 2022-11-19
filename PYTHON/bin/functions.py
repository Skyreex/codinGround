def hello(a, b):
    a = a.title()
    print(f"Hello {a}, you're {b} years old")
    return

name = input("Enter your name : ")
age = int(input("Enter your age : "))
hello(name, age)
