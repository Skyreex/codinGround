# from oop.EX.pkg.vaccin import Vaccin
from oop.EX.pkg.dose import Dose


class CentreVaccination(Dose):
    def __init__(self, __nomCentre, __adresse, listVaccin=None, listVacciné=None, listDose=None):
        if listDose is None:
            listDose = []
        if listVacciné is None:
            listVacciné = []
        if listVaccin is None:
            listVaccin = []
        self.__nomCentre = __nomCentre
        self.__adresse = __adresse
        self.listVaccin = listVaccin
        self.listVacciné = listVacciné
        self.listDose = listDose

    def Affichage(self):
        print(f"Centre : {self.__nomCentre}\nAdresse : {self.__adresse}\n"
              f"Liste Vaccin : {self.listMeth(self.listVaccin)}\nListe vacciné : {self.listMeth(self.listVacciné)}\n"
              f"Liste dose : {self.listMeth(self.listDose)}")

    @staticmethod
    def listMeth(list):
        l = []
        for i in list:
            l.append(i.display())
        return l

    @property
    def getNomcentre(self):
        return self.__nomCentre

    @getNomcentre.setter
    def setNomcentre(self, temp):
        self.__nomCentre = temp

    @property
    def getAdresse(self):
        return self.__adresse

    @getAdresse.setter
    def setAdresse(self, temp):
        self.__adresse = temp

    def addVaccin(self, temp):
        self.listVaccin.append(temp)

    def searchVaccin(self, temp):
        for i in self.listVaccin:
            if temp == i.getCodeV:
                return True
            else:
                return False

    def addVacciné(self, temp):
        self.listVacciné.append(temp)

    def searchVacciné(self, p):
        for i in self.listVacciné:
            if p == i.getCin:
                return True
            else:
                return False

    def delVacciné(self, p):
        val = -1
        for i in self.listVacciné:
            val += 1
            if p == i.getCin:
                self.listVacciné.pop(val)

    def delVaccin(self, p):
        val = -1
        for i in self.listVaccin:
            val += 1
            if p == i.getCodeV:
                self.listVaccin.pop(val)

    def addDose(self, temp):
        self.listDose.append(temp)
