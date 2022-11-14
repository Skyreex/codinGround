fruits = ["apple", "banana", "cherry"]  # list
x, y, z = fruits

print(x)
print(y)
print(z)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
