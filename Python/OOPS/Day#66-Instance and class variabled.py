# class MyClass:
#     class_variable = 0
    
#     def __init__(self):
#         MyClass.class_variable += 1

#     def print_class_variable(self):
#         print(MyClass.class_variable)
        

# obj1 = MyClass()
# obj2 = MyClass()

# obj1.print_class_variable() # Output: 2
# obj2.print_class_variable() # Output: 2

# Class Variables

# class Employee:
#     team = 'SSE'

#     def __init__(self,name):
#      self.name = name

#     def QA_Automation(self):
#         self.skills = ['API', 'Postman']

#     def QA_manual(self):
#         self.skills = ['Sanity', 'Regression']

# automation = Employee("Durgesh")
# print(f"({automation.name} is an QA_Automation engineer from {Employee.team} team")

# automation2 = Employee("Rahul")
# print(f"({automation2.name} is an QA_Automation engineer from {Employee.team} team")

#instance Variables

class Employee:
    team = 'SSE'

    def __init__(self,name):
     self.hike= 0.5
     self.name = name

    def QA_Automation(self):
        self.skills = ['API', 'Postman']

    def QA_manual(self):
        self.skills = ['Sanity', 'Regression']

automation = Employee("Durgesh")
automation.hike = 10
Employee.team = "RBI"
print(f"{automation.name} is an QA_Automation engineer from {Employee.team} team with increment hike of {automation.hike}")

automation2 = Employee("Rahul")
print(f"{automation2.name} is an QA_Automation engineer from {Employee.team} team")





















