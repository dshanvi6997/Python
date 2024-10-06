# import math
# class Circle:
#     def __init__(self, radius):
#         self.radius=radius

#     def area(self):
#      return math.pi*(self.radius**2)

#     def parameter(self):
#      return 2*math.pi*self.radius

# r1 = Circle(3)
# print(r1.area())
# print(r1.parameter())

#____________________________________________________________________________________

# class Employee:
#     def __init__(self,role,department,salary):
#      self.role = role
#      self.department = department
#      self.salary = salary

#     def showDetails(self):
#      print("Role = ",self.role) 
#      print("Dep = ",self.department)
#      print("Sal = ",self.salary)

# class Engineer(Employee):
#     def __init__(self, name, age):
#        self.name = name
#        self.age = age
#        super().__init__("Engineer" , "IT" , "75,000")
       
# # e1 = Employee("Accountant", "Finance", "30,000")
# # e1.showDetails()
# e1 = Engineer("Durgesh",27)
# print(e1.name)
# print(e1.age)
# e1.showDetails()

#________________________________________________________________________

class Store:
    def __init__(self, item, price):
      self.item = item
      self.price = price

    def __gt__(self, q2):
       return self.price > q2.price

q1 = Store("apple", 30)
q2 = Store("ornage", 100)
print(q1 > q2)
