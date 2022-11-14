a = "YoU"
b = "live"
moto = f" {a} only {b} once "

print(len(moto))
print(moto.upper())
print(moto.lower())
print(moto.title())
print(moto)
print(moto.strip())  # .Strip remove space character from the start and the end/ .rstrip end space / .lstrip start space
print(moto.lstrip().upper())
print(moto.find("once"))
print(moto.replace("once", "twice").upper().strip())
print(moto.upper().strip())