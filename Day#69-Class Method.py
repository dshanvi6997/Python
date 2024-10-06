#Class Mehtods

# class Student:
#     name = 'unknown'

#     def changeName(self,name):
#         self.name = name

# c = Student()
# c.changeName("rahul")
# print(c.name)
# print(Student.name)

#__________________________________________________________________

# class Student:
#     name = 'unknown'

#     def changeName(self,name):
#         Student.name = name

# c = Student()
# c.changeName("rahul")
# print(c.name)
# print(Student.name)

#__________________________________________________________________

# class Student:
#     name = 'unknown'
    
#     @classmethod
#     def changeName(cls,name):
#      cls.name = name

# c = Student()
# c.changeName("rahul")
# print(c.name)
# print(Student.name)

class Employee:
  company = "Apple"
  def show(self):
    print(f"The name is {self.name} and company is {self.company}")

  @classmethod
  def changeCompany(cls, newCompany):
    cls.company = newCompany


e1 = Employee()
e1.name = "Harry"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)