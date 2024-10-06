# class Car:
#     def __init__(self,type):
#      self.type=type

#     @staticmethod
#     def start():
#         print("Car Started")

#     @staticmethod
#     def stop():
#         print("Car stopped")

# class ToyotaCar(Car):
#    def __init__(self, name,type):
#       super().__init__(type)
#       self.name=name

# t1 =ToyotaCar('prius','electric')
# print(t1.type)

# area, cube , volumne of a square

class Square:
    def __init__(self,side):
        self.side = side

    def area(self):
     area_square = self.side*self.side
     return area_square
        
class Cube(Square):
    def __init__(self,side):
        super().__init__(side)

    def Volumne(self):
     area_square = self.side*self.side*self.side
     return area_square

v1 = Cube(3)  
print(v1.area())
print(v1.Volumne())      