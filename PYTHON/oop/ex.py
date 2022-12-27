import math


class Point:
    nb = 0

    def __init__(self, abs, ord):
        self.__abs = abs
        self.__ord = ord
        Point.nb += 1

    def __str__(self):
        return f"x = {self.__abs} y = {self.__ord}"

    @property
    def getAbs(self):
        return self.__abs

    @property
    def getOrd(self):
        return self.__ord

    @getAbs.setter
    def setAbs(self, x):
        self.__abs = x

    @getOrd.setter
    def setOrd(self, y):
        self.__ord = y

    def __eq__(self, pt):
        return (self.__abs == pt.getAbs) and (self.__ord == pt.getOrd)

    def calculerdistance(self, B):
        distance = math.sqrt(pow((self.__abs - B.getAbs), 2) + pow((self.__ord - B.getOrd), 2))
        return distance

    def calculermilieu(self, pt):
        M.setAbs = (self.__abs + pt.getAbs) / 2
        M.setOrd = (self.__ord + pt.getOrd) / 2
        return M


class TroisPoints(Point):
    def __init__(self, point1, point2, point3):
        self.__point1 = point1
        self.__point2 = point2
        self.__point3 = point3

    def __str__(self):
        return f"{self.__point1} // {self.__point2} // {self.__point3}"

    @property
    def getP1(self):
        return self.__point1

    @property
    def getP2(self):
        return self.__point2

    @property
    def getP3(self):
        return self.__point3

    @getP1.setter
    def setP1(self, P):
        self.__point1 = P

    @getP2.setter
    def setP2(self, P):
        self.__point2 = P

    @getP3.setter
    def setP3(self, P):
        self.__point3 = P

    def sontalignes(self):
        return self.getP1.calculerdistance(self.getP3)
        # return (AB == AC + BC) or (AC == AB + BC) or (BC == AC + AB)


p1 = Point(1, 7)
p2 = Point(4, 5)
M = Point(0, 0)
print(p1)
p1.setOrd = 3
p3 = p1
print(p1 == p3)
print(p1.calculerdistance(p2))
M = p1.calculermilieu(p2)
print(M)
p4 = Point(3, 6)
P1 = TroisPoints(p1, p2, p3)
print(P1)
P1.setP3 = p4
print(P1)
print(P1.sontalignes)
print("Hello")
print(P1.getP3)
AC = P1.getP1.calculerdistance(P1.getP3)
AB = P1.getP1.calculerdistance(P1.getP2)
BC = P1.getP2.calculerdistance(P1.getP3)
print(AC, AB, BC)
