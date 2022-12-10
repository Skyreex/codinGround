price = int(input("Please enter the price : "))
discount = input("Please enter the discount : ")
val = len(discount)

if discount[val-1] == "%":
    discount = discount[0:val-1]

discount = int(discount)
discount /= 100
new_price = price * (1-discount)
print(f"The new price is {int(new_price)}")
