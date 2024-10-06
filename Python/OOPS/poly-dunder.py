class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(f"{self.real}i + {self.img}j")
    
    def __sub__(self,num2):
     newreal = self.real - num2.real
     newimg = self.img - num2.img
     return Complex(newreal,newimg)

num1 = Complex(9,4) 
num2 = Complex(4,5)    
num3 = num1 - num2
num3.showNumber()

