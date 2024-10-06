#  Function Arguments and return statement

# 1. Default Argument 2. keyword 3. variable length argument 4. required argument

# Default Argument 

# def name(fname) :
#  print("my name is", fname )
    
# name("Durgesh")
# name("sharma")

# def my_function(fname, lname):
#   print(fname , lname)

# my_function("Emil", "Refsnes")
# def name(fname="durgesh", mname="sagar" , lname="sharma"):
#   print("My full name is :" , fname, mname, lname)
# name()

# def my_function(*,x):
#   print(x)

# my_function(x = 3)

#2. keyword 

# def name(fname, mname, lname):
#   print("My full name is :" , fname, mname, lname)
# name(mname ="Dyurfesh", lname="sharma", fname ="asd")

#3. variable length argument 
# Arbitrary Arguments:

# def name(*name):
#   print("Enter your full name :" ,name[0], name[1],name[2])
# name("durgesh", "sharma", "Sagar")

# def name(*name):
#   print("Enter your full name :" + name[2])
# name("durgesh", "sharma", "Sagar")

# #Keyword Arbitrary Arguments:

# def name(**name):
#   print("Enter your full name :" ,name['fname'], name['mname'], name['lname'])
# name(fname="kapil", mname="yadav", lname="san")

# def my_function(fruits):
#   for x in fruits:
#     print(x)

# fruits = ["apple", "banana", "cherry"]
# my_function(fruits)

#Return function

def num3(x):
 z=x-1
 return z

def num1(a,b):
 c=a+b
 return c
num=num1(2,3)
final_num = num3(num)
print(final_num)

















    



