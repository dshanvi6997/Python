# Example 1: Taking the Name and Age of the user as input and printing it.

name = input("Enter your Name\n")
print("My name is :", name)
age = input("Enter Your Age\n")
print("My age is :", age)

# Example 2: Taking two String from users.

num1 = input("Enter first number : ")
num2 = input("Enter second number : ")
print("Sum of two number is :", str(num1) + str(num2))

# Example 3: Taking two integers from users and perform arithmetic alloperations.

num1 = input("Enter first number :")
num2 = input("Enter second number :")
print("Sum of first and second number is :", float(num1) + float(num2))
print("Subtraction of first and second number is :", float(num1) - float(num2))
print("Multiplication of first and second number is :", float(num1) * float(num2))
print("Division of first and second number is :", float(num1) * float(num2))
print("Full Division of first and second number is :", float(num1) * float(num2))
print("Modulus of first and second number is :", float(num1) * float(num2))
print("Exponential of first and second number is :", float(num1) * float(num2))

# Calculator

num1 = int(input("Enter first number :"))
Operator = input("Select Your Operator (+,-,*,/,//,**) :")
num2 = float(input("Enter second number :"))

if Operator == '+':
 print("Sum to first and second is :", num1+num2)
elif Operator == '-':
 print("Sub to first and second is :", num1-num2)
elif Operator == '*':
 print("Mul to first and second is :", num1*num2)
elif Operator == '/':
 print("Div to first and second is :", num1/num2)
elif Operator == '//':
 print("Full Div to first and second is :", num1//num2)
elif Operator == '**':
 print("Expoenetial to first and second is :", num1**num2)
else:
 print("Entered operator is not valid")