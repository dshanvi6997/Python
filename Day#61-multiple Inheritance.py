class A:
    VarA= "Class A is called"
    
class B:
    VarB= "Class B is called"
    
class C(A,B):
    VarC= "Class C is called"   
    
c1 = C()   
print(c1.VarA)
print(c1.VarB)
print(c1.VarC)

#-----------------------------------------------------------------

class Mother:
    mothername = ""
 
    def mother(self):
        print(self.mothername)
 
 
class Father:
    fathername = ""
 
    def father(self):
        print(self.fathername)
 
 
class Son(Mother, Father):
    def parents(self):
        print("Father name is :", self.fathername)
        print("Mother :", self.mothername)
s1 = Son()
s1.fathername = "Mommy"
s1.mothername = "Daddy"
s1.parents()