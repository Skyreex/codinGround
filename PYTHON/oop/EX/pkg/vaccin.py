class Vaccin:
    no_of_vaccin = 0

    def __init__(self, __codeV, __nomV, __dureeV):
        self.__codeV = __codeV
        self.__nomV = __nomV
        self.__dureeV = __dureeV
        Vaccin.no_of_vaccin += 1

    def Affichage(self):
        print(f"CodeV : {self.__codeV}\nNomV : {self.__nomV}\nDuréeV : {self.__dureeV} months")

    def display(self):
        return f"CodeV : {self.__codeV} // NomV : {self.__nomV} // DuréeV : {self.__dureeV} months"

    @property
    def getCodeV(self):
        return self.__codeV

    @getCodeV.setter
    def setCodeV(self, temp):
        self.__codeV = temp

    @property
    def getNomV(self):
        return self.__nomV

    @getNomV.setter
    def setNomV(self, temp):
        self.__nomV = temp

    @property
    def getDuree(self):
        return self.__dureeV

    @getDuree.setter
    def setDuree(self, temp):
        self.__dureeV = temp
