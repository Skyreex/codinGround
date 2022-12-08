msg = input("msg : ")
key = int(input("key : "))
msg2 = ""
for i in msg:
    msg2 = msg2 + chr(ord(i)+key)
print(msg)
print(msg2)
