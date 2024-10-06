
# Python Convert String to float
# string = "234.23"
# convertintofloat = float(string)
# print(convertintofloat)
# print(type(convertintofloat))

# Addition of string and integer Using Explicit Conversion

# string= "1.2"
# num1 = 1
# #num2 = float(string)
# print(float(string)+num1)

# Calculator with all Arithmatic Operations

number1 = input("Enter your first number : ")
operator = input('Please select your won operator "+,-,/,*,**,//" :')
number2 = input("Enter your second number : ")

if operator == '+' :
    new1 = float(number1)
    new2 = float(number2)
    print('Addition of two number is : ', new1+new2)
elif operator == '-' :
    print('Subtractionn of two number is : ', float(number1)-float(number2))
elif operator == '*':
    print('multiplication of two number is : ', float(number1)-float(number2))
elif operator == '**' :
    print('Exponential of two number is : ', float(number1)**float(number2))
elif operator == '/' :
    print('Division of two number is : ', float(number1)/float(number2))
elif operator == '//' :
    print('Full Division of two number is : ', float(number1)//float(number2))
elif operator == '%' :
    print('Subtractionn of two number is : ', float(number1)%float(number2))
else:
    print('** Error Error Error** : Selected operator is not valid ')
    





