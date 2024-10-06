# Default function

def num(a,b,c=3):
    print("Addition of all the number :", (a+b+c)/2)
num(1,3)

def num(fname , mname="Sagar" , lname ="Sharma" ):
 print("My full name is :", fname, mname, lname)
num("Durgesh")

# Keyword Argument

def gmean(a,b,c):
    print("gmean of three number is", (a+b+c)/3)
gmean(b=3,c=3,a=4)

def name(fname , mname , lname):
    print("my full anme is :", fname , mname , lname)
name(lname='sharma', fname='durgesh', mname= 'sagar')

# required function 

def name(fname , mname , lname):
    print("my full anme is :", fname , mname , lname)
name(lname='sharma', mname= 'sagar')

# Variable length Argument

# 1. Arbitatory Functions

def name(*name):
    print("my full anme is :", name[0] , name[1] , name[2])
name('sharma','sagar','Durgesh')

# 2. Keyword arbitatory functions

def name(**name):
    print("My full name is :" ,name['fname'],name['mname'], name['lname'])
name(fname='sharma',lname='sagar',mname='Durgesh')
