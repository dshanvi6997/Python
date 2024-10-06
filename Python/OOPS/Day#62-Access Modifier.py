# Public Variable

# class Student:
#     # constructor is defined
#     def __init__(self, age, name):
#         self.age = age               # public variable
#         self.name = name             # public variable
# obj = Student(21,"Harry")
# print(obj.age)
# print(obj.name)

# Private Variable

class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # private variable
        self.__name = name             # private variable
    
    def __marks(self):
        print("Total Marks")
      
obj = Student(21,"Harry")
print(obj.age)
print(obj.__name)
obj.__marks
obj._Student__marks   ## Not a valid code


#Name Manglingclass Student:

# class Student:
#     # constructor is defined
#     def __init__(self, age, name):
#         self.age = age               # private variable
#         self.__name = name             # private variable
# obj = Student(21,"Harry")
# print(obj.age)
# print(obj._Student__name)

#Private variables

class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())