from oop.EX.pkg.vacciné import Vacciné


class Dose(Vacciné):
    def __init__(self, __object, __vacobject, __coded, __date1std, __dateeffet2ndd):
        super().__init__(__object, __vacobject, __date1std)
        self.__coded = f"{__vacobject.getCodeV}{__coded}"
        self.__date1std = __date1std
        self.__date2ndd = f"{int(__date1std[0:2]) + 15}{__date1std[2:]}"
        self.__dateeffet2ndd = __dateeffet2ndd

    def Affichage(self):
        print(f"Vacciné : {self.getCin}\nCodeD : {self.__coded}\n"
              f"Date 1er Dose : {self.__date1std}\nDate 2nd Dose : {self.__date2ndd}\n"
              f"Date effet 2nd Dose : {self.__dateeffet2ndd}")

    def display(self):
        return f"Vacciné : {self.getCin} // CodeD : {self.__coded} // " \
               f"Date 1er Dose : {self.__date1std} // Date 2nd Dose : {self.__date2ndd} " \
               f"// Date effet 2nd Dose : {self.__dateeffet2ndd}"

    @property
    def getCoded(self):
        return self.__coded

    @getCoded.setter
    def setCoded(self, temp):
        self.__coded = temp

   # @property
   # def getVaccine(self):
#       return self.__vaccine

   # @getVaccine.setter
   # def setVaccine(self, temp):
#    self.__vaccine = temp

  #  @property
  #  def getVaccin(self):
  #      return self.__vaccin

   # @getVaccin.setter
   # def setVaccin(self, temp):
   #     self.__vaccine = temp

    @property
    def getDate1std(self):
        return self.__date1std

    @getDate1std.setter
    def setDate1std(self, temp):
        self.__date1std = temp

    @property
    def getDate2ndd(self):
        return self.__date2ndd

    @getDate2ndd.setter
    def setDate2ndd(self, temp):
        self.__date2ndd = temp

    @property
    def getDateeffet2ndd(self):
        return self.__dateeffet2ndd

    @getDateeffet2ndd.setter
    def setDateeffet2ndd(self, temp):
        self.__dateeffet2ndd = temp
