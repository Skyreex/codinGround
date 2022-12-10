cc_num = input("Enter your credit card number : ")
cc_hidden = ""
T = []
new_cc = cc_num[0:4]
counter = 0
for number in cc_num:
    counter += 1
    if counter <= 4:
        T.append(0)
        cc_hidden += number
    else:
        T.append(ord(number)-42)
        cc_hidden += "*"

for i in T:
    if i == 0:
        continue
    else:
        new_cc += chr(42+i)

print(cc_hidden)
print(cc_num)
print(new_cc)
print(T)


# * = 42
