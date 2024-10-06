# Delete Objects

# class Student:
#     def __init__(self, name):
#         self.name = name

# s1=Student("durgesh")
# print(s1.name)
# del s1.name      
# print(s1.name)

# Private Attribute

# class Student:
#     def __init__(self, name, deg, age):
#         self.name = name
#         self.__deg = deg
#         self.age = age

#     def profile(self):
#         print(self.__deg)

# s1=Student("durgesh", 'QA', 36)
# print(s1.name)
# print(s1.__deg)
# print(s1.age)

# Private Methods

class Student:
   __name='anonymous'
   print(__name)

   def __hello(self):
      print("Hello user how are you")

   def Welcome(self):
        self.__hello()
   
s1 = Student()
print(s1.Welcome())


# print(s1.__hello)
# print(__name)

