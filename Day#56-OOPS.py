# class SSE:
#    Project_Name = "SSE"
    
#    def __init__(self, name, skills ,total_exp):
#       self.name= name
#       self.skills = skills
#       self.total_exp = total_exp

   
# qasse1 = SSE("durgesh", ['API','Postman'], " 4 Years")
# print(f"Name of the emp : {qasse1.name}")
# print(f"Skills of the emp : {qasse1.skills}")
# print(f"Total_Exp of the emp : {qasse1.total_exp}")

# qasse2 = SSE("Shubham", ['API','Postman','Manual'], " 8 Years")
# print(f"Name of the emp : {qasse2.name}")
# print(f"Skills of the emp : {qasse2.skills}")
# print(f"Total_Exp of the emp : {qasse2.total_exp}")


class Person:
  name = "Durgesh"
  occupation = "QA Engineer"
  exp = 4

  def info(self):
    print(f"{self.name} is a {self.occupation} with {self.exp} Year of experiance" )

p1 = Person()
p1.info()

p2 = Person()
p2.name = "Diksha"
p2.occupation = "Automation Engineer"
p2.exp = 6
p2.info()