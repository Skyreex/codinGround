class Person:
    def __init__(self, __cin, __Fname, __Lname):
        self.__cin = __cin
        self.__Fname = __Fname
        self.__Lname = __Lname

    def __str__(self):
        return f"{self.__Fname} {self.__Lname} // {self.__cin}"

    @property
    def getCin(self):
        return self.__cin

    @getCin.setter
    def setCin(self, temp):
        self.__cin = temp
        return self.__cin

    @property
    def getFname(self):
        return self.__Fname

    @getFname.setter
    def setFname(self, temp):
        self.__Fname = temp
        return self.__Fname

    @property
    def getLname(self):
        return self.__Lname

    @getLname.setter
    def setLname(self, temp):
        self.__Lname = temp
        return self.__Lname


class centreVaccination(Person):
    def __init__(self, nomCentre, adresse, listVaccin, listVacciné, listDose):
        self.nomCentre = nomCentre
        self.adresse = adresse
        self.listVaccin = []
        self.listVacciné = []
        self.listDose = []

    def __str__(self):
        return f"Centre : {self.nomCentre}\nAdresse : {self.adresse}\n" \
               f"Liste Vaccin : {self.listVaccin}\nListe vacciné : {self.listVacciné}\n" \
               f"Liste dose : {self.listDose}"

    def addVaccin(self, temp):
        if isinstance(temp, str):
            self.listVaccin.append(temp)
        else:
            for i in temp:
                self.listVaccin.append(i)

    def searchVaccin(self, vaccin):
        if vaccin in self.listVaccin:
            return True
        else:
            return False

    def addVacciné(self,p):
        self.listVacciné.append(p.getCin)


    def searchVacciné(self,p):
        if p.getCin in self.listVacciné:
            return True
        else:
            return False

Vs = ["Pfizer", "Astrazenica", "Johnson"]
V = "Sinopharme"
p1 = Person("BK12412", "aaa", "AAA")
p2 = Person("BK43412", "bbb", "BBB")
c1 = centreVaccination("AAA", "BBB", "", "","" )
codeVaccin = "Pfizer"
c1.addVaccin(Vs)
c1.addVaccin(V)
c1.addVacciné(p1)
 


print(p1)
print(c1)
print(c1.searchVaccin(codeVaccin))
print(c1.searchVacciné(p1))
