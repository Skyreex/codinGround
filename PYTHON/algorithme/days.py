class Day(object):
    def day_1(self):
        print("Monday")
    def day_2(self):
        print("Tuesday")
    def day_3(self):
        print("Wednesday")
    def day_4(self):
        print("Thursday")
    def day_5(self):
        print("Friday")
    def day_6(self):
        print("Saturday")
    def day_7(self):
        print("Sunday")
    def getDay(self,no):
        name_of_method="day_"+str(no)
        method=getattr(self,name_of_method,lambda :'Give an input as an integer from 1 to 7')
        return method()

mo=Day()
mo.getDay(input("n : "))
