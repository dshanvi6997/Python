class Student:
    def __init__(self,math,phy,chem):
        self.math = math
        self.phy=phy
        self.chem=chem

    # @property
    def percentage(self): 
        return str((self.math+self.phy+self.chem)/3) +'%'

stu1 = Student(23,56,89)
print(stu1.percentage())

stu1.math= 56
print(stu1.percentage())





