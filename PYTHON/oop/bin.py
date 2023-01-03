class A:
    def __init__(self, __x, __y):
        self.__x = __x
        self.__y = __y

    def __str__(self):
        return f"{self.__x} / {self.__y}"

    @property
    def getx(self):
        return self.__xy

    @property
    def gety(self):
        return self.__y

    @gety.setter
    def sety(self, temp):
        self.__y = temp


p = A(1, 4)
p2 = A(2, 6)
p.sety = 55
print(f"{p} \n{p2}")
