salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")


def num(a,b):
 if a>b:
    print("A is greater")
 else:
    raise ValueError(f"{a} is not greater than {b}")    

a = int(input("enter 1 num: "))
b = int(input("enter 2 num: "))
num(a,b)


list = [1,2,3,4,5,6]
try:
 for i in list:
   i = int(input("Enter i value: "))
   print(f"Index value of {i} is: ", list[i])
except:   
   raise Exception("Not found")

n=5
if 2/n==0 :
 print("Answer is: ")
else:
 raise Exception(f"cannot be divisible by {n}")
