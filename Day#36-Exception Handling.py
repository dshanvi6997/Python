'''In Python, there are several built-in Python exceptions that can be raised when an error occurs during the execution of a program. Here are some of the most common types of exceptions in Python:

SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a 
missing colon, or an unbalanced parenthesis.

TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a 
string to an integer.

NameError: This exception is raised when a variable or function name is not found in the current scope.

IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.

KeyError: This exception is raised when a key is not found in a dictionary.

ValueError: This exception is raised when a function or method is called with an invalid argument or input, such as trying to 
convert a string to an integer when the string does not represent a valid integer.

AttributeError: This exception is raised when an attribute or method is not found on an object, such as trying to access a 
non-existent attribute of a class instance.

IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.

ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.

ImportError: This exception is raised when an import statement fails to find or load a module. '''

# try:
#     num = int(input("Please enter an integer : "))
# except ValueError:
#     print("No")

# try:
#     num = int(input("Enter an integer: "))
# except ValueError:
#     print("Number entered is not an integer.")

# marks = 10000
# a = marks / 0
# print(a) #ZeroDvisionError

# x = 5
# y = "hello"
# z = x + y  #typeerror


# x = 5
# y = "hello"
# try:
#  z = x + y
# except :
#  print(f"String {y} cannot be added to integer {x}")

# a = [1, 2, 3]
# try: 
#     print ("Second element = ", a[1])

#     print ("Fourth element = ", a[3])

# except:
#     print ("An error occurred")

# def fun(a):
#     if a < 4:

#         b = a/(a-3)
#     print("Value of b = ", b)
    
# try:
#     fun(3)
#     fun(5)
# except ZeroDivisionError:
#     print("ZeroDivisionError Occurred and Handled")
# except NameError:
#     print("NameError Occurred and Handled")    


# def AbyB(a , b):
#     try:
#         c = ((a+b) / (a-b))
#     except ZeroDivisionError:
#         print ("a/b result in 0")
#     else:
#         print (c)
# AbyB(2.0, 3.0)
# AbyB(3.0, 3.0)


# try: 
#     raise NameError("Hi there")
# except NameError:
#     print ("An exception")
#     raise    

#NameError
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

