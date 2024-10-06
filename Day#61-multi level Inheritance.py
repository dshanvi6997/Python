# Multi level inheritance

class Cricket:
    mens_teams = 20
    womens_teams = 20


    def Bat(self):
        return "Both the Teams Play with bat  :"

    @staticmethod
    def Ball():
        return "Both the Teams Play with ball :"


class Mens(Cricket):
    def __init__(self,ODI, T20):
        self.ODI = ODI
        self.T20 = T20

class Womens(Cricket):
    def __init__(self,test, T10):
        self.ODI = test
        self.T10 = T10

m1=Womens('unlimited','10-10') 
print(m1.ODI)
print(m1.Bat())
print(m1.Ball())
m1=Mens('50-50','20-20')
print(m1.T20)
print(m1.Ball())

#_-------------------------------------------------------

class Parent:
    def func1(self):
        print("This function is in parent class.")
 
class Child(Parent):
    def func2(self):
        print("This function is in child class.")
 
object = Child()
object.func1()
object.func2()

#_____________________________________________________________________


class Grandfather:
 
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername
 
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        Grandfather.__init__(self, grandfathername)

class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Father.__init__(self, fathername, grandfathername)
 
    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)
        
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()