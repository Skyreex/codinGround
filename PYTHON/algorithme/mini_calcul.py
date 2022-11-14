a = int(input("a : "))
b = int(input("b : "))
ope = input("Veuillez entrer l'opérateur : ")

match ope:
    case "+":
        print(f"{a} + {b} = {a + b}")
    case "-":
        print(f"{a} - {b} = {a - b}")
    case "/":
        if b != 0:
            print(f"{a} / {b} = {a / b}")
        else:
            print("error")
    case "*":
        print(f"{a} * {b} = {a * b}")
    case _:
        print("error")

