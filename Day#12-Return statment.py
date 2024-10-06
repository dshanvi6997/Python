def num(a,b):
    print("Addition of two number :", a+b)
num(2,3)


def num(a,b):
    c=a/b
    return c
finalnumber=num(3,4)
print(finalnumber)

def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

fullanme = name("James", "Buchanan", "Barnes")
print(fullanme)


# Making use of return statment on another function

def num(c):
    return c-1

def num2(a,b):
    mean = (a+b)/2
    return mean    #  return menthod will return the value for call function
num1=num2(2,3)
finaloutput=num(num1)
print(finaloutput)




