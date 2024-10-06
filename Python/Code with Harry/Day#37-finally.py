# def num(n,m):
#  try:
#   number = n/m
#   print(f"{n} divided by {m} is : ", number)
#  except:
#   print(f"{n} cannot be divisible by Zero")
#  finally :
#   print("Exit the loop")  
# n = float(input("Enter first number :"))
# m = float(input("Enter Second number :"))  
# num(n,m)


# try:
#   number = int(input("Enter number :"))
# except ValueError:
#   print("Entered number is not an integer")
# else:
#    print("Integer Accepted")  
# finally:
#   print("Out of the loop")  



try:
    list=[3,4,5,6,7]
    for i in list :
        i = int(input("Enter your number: "))
        print("List Executed: ", list[i])
except:
    print("Not executed") 
    

finally:
    print('i will always be executed') 



# def fun():
#  try:
#     list=[3,4,5,6,7]
#     for i in list :
#         i = int(input("Enter your number: "))
#         print("List Executed: ", list[i])
#         return 1
#  except:
#     print("Not executed") 
#     return 0 

#  finally:
#     print('i will always be executed') 
# # print("I will always get executed") 

#  x= fun()  
#  print(x)          
