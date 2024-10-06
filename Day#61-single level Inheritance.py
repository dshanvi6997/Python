# Inhertiance

class Car:
    color = "Black"

    @staticmethod
    def start():
        print("Car Started")

    @staticmethod
    def stop():
        print("Car stopped")


class toyotaCar(Car):
    def __init__(self, name):
        self.name= name

c1 = toyotaCar("fortuner")  
c1.start()  

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=====

class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id 

  def showDetails(self):
    print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
  def showLanguage(self):
    print("The default langauge is Python")


e1 = Employee("Rohan Das", 400)
e1.showDetails()
e2 = Programmer("Harry", 4100)
e2.showDetails()
e2.showLanguage()


