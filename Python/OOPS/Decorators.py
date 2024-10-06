# # defining a decorator
# def hello_decorator(func):

#     # inner1 is a Wrapper function in 
#     # which the argument is called
    
#     # inner function can access the outer local
#     # functions like in this case "func"
#     def inner1():
#         print("Hello, this is before function execution")

#         # calling the actual function now
#         # inside the wrapper function.
#         func()

#         print("This is after function execution")
        
#     return inner1


# # defining a function, to be called inside wrapper
# def function_to_be_used():
#     print("This is inside the function !!")


# # passing 'function_to_be_used' inside the
# # decorator to control its behaviour
# function_to_be_used = hello_decorator(function_to_be_used)


# # calling the function
# function_to_be_used()

# #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# import time

# def timer(func):
#     def wrapper(*args):
#      start = time.time()
#      print(f"time started and start time is {start}")
#      result = func(*args)
#      end = time.time()
#      print(f"time ended and start time is {end}")
#      print (f"time taken is {end - start}")
#      return result
#     return wrapper    

# @timer
# def time_function(n):
#  time.sleep(n)
# time_function(3)    


#--------------------------------------------------------------------------------

import time
def company(func):
   def qualification(*args, **rwargs):
     join_time= time.time()

     print(f"{join_time} of {args[0]} is : ")  # Main function

     result = func(*args, **rwargs)
     return result
   return qualification

@company
def emp(name, skills=None, age=26):
   if skills is None:
      skills = ['Manual', 'API']
   print(f"{name} is the employee with {skills} skills under the age {age}")
emp("Durgesh")


