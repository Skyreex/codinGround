try:
    number = int(input("Enter a number : "))
    val = 10 / 0
    print(number)
except ZeroDivisionError:
    print("can't divide by 0")
except ValueError:
    print("Invalid input")
