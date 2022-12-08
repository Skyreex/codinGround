num1 = float(input("Enter first number: "))
op = input("Enter first number: ")
num2 = float(input("Enter second number: "))

match op:
    case "/":
        if num2 != 0:
            print(f"{num1} {op} {num2} = {num1/num2}")
        else:
            print("Can't divide by 0")
    case "*":
        print(f"{num1} {op} {num2} = {num1 * num2}")
    case "+":
        print(f"{num1} {op} {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} {op} {num2} = {num1 - num2}")
    case _:
        print("Invalid operator")
