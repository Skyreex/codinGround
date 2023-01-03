class Person:
    no_of_person = 0

    def __init__(self, __cin, __Fname, __Lname):
        self.__cin = __cin
        self.__Fname = __Fname
        self.__Lname = __Lname
        Person.no_of_person += 1

    def Affichage(self):
        print(f"Fname : {self.__Fname}\nLname : {self.__Lname}\nCIN   : {self.__cin}")

    def display(self):
        return f"Fname : {self.getFname}\nLname : {self.getLname}\nCIN   : {self.getCin}"

    def Display(self):
        return f"Fname : {self.getFname} // Lname : {self.getLname} // CIN   : {self.getCin} // "

    @property
    def getCin(self):
        return self.__cin

    @getCin.setter
    def setCin(self, temp):
        self.__cin = temp

    @property
    def getFname(self):
        return self.__Fname

    @getFname.setter
    def setFname(self, temp):
        self.__Fname = temp

    @property
    def getLname(self):
        return self.__Lname

    @getLname.setter
    def setLname(self, temp):
        self.__Lname = temp