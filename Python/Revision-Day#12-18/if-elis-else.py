'''Write a program that takes time as input from user in 24 hours clock format like: 1900 = 7pm. Implement the following 
case using if, else & else if statements'''


# time = int(input("Enter your time :"))

# import time
# x= time.strftime('%H:%M:%S')
# print(x)

# if x >=0000 and x <1200 :
#     print("Good morning")
# if x >=1200 and x <1700 :
#     print("Good Afternoon")
# if x >=1700 and x <2100 :
#     print("Good evening")
# if x >=2100 and x <2359 :
#     print("Good Night")





import time
timestamp = time.strftime("%I %p")
if timestamp  :
 print("Good Morning")
else :
 print("Need more information")


# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)




