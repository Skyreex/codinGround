weight = float(input("weight : "))

while weight < 0:
    weight = float(input("weight : "))
cal = weight*1.3*24
print("calories needed :")
print(cal)
pro = weight*2
print("protein needed")
print(pro)
car = weight*4
print("carbs needed")
print(car)
fat = car
print("fats needed")
print(fat)

