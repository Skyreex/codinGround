from oop.EX.pkg.Personne import Person
from oop.EX.pkg.vaccin import Vaccin


class Vacciné(Person, Vaccin):
    no_of_vacciné = 0

    def __init__(self, __object, __vacobject, __dateV):
        Person.__init__(self, __object.getCin, __object.getFname, __object.getLname)
        Vaccin.__init__(self, __vacobject.getCodeV, __vacobject.getNomV, __vacobject.getDuree)
        self.__dateV = __dateV
        Vacciné.no_of_vacciné += 1

    def Affichage(self):
        print(f"{Person.display(self)}\nCodeV : {self.getCodeV}\nDateV : {self.__dateV}")

    def display(self):
        return f"{Person.Display(self)} // CodeV : {self.getCodeV} // DateV : {self.__dateV}"



    @property
    def getDateV(self):
        return self.__dateV

    @getDateV.setter
    def setDatev(self, temp):
        self.__dateV = temp
