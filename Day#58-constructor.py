# 1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
# Area of a circle = πr2. The perimeter of a circle = 2πr

# import math
# class Circle:

#     def __init__(self,radius):
#         self.radius = radius       

#     def area(self):
#         return math.pi*self.radius**2

#     def perimeter(self):
#         return 2*math.pi*self.radius
    
# radius1 = float(input("Enter the radius of the Circel1 :"))     

# circle1 = Circle(radius1)
# print("Area of a Circle is : " , circle1.area())
# print("Area of a perimeter is : ", circle1.perimeter())
        
# radius2 = float(input("Enter the radius of the Circel2 :")) 

# circle2 = Circle(radius2)
# print("Area of a Circle is : " , circle2.area())
# print("Area of a perimeter is : ", circle2.perimeter())

'''2. Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method 
to determine the person's age.'''

#Age formula = Given date - Date of birth.

from datetime import datetime
current_date = datetime.now().date()

class person:

    def __init__(self,name, country):
        self.name = name 
        self.country = country

    def age(self):
        return current_date.year-date_object.year
    
date_input = input("Enter a date (YYYY-MM-DD): ")
date_object = datetime.strptime(date_input, "%Y-%m-%d").date()

person_details = person("Durgesh","India")
print(f"Name of the person is {person_details.name} he is from {person_details.country} and his age is {person_details.age()} Years")


