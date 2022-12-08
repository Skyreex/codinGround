password = open("data.txt", "r")
# print(password.read())
for log in password.readlines():
    print(log)
password.close()

password = open("data.txt", "r")
print(password.readline())
logs = password.readlines()
print(logs)
