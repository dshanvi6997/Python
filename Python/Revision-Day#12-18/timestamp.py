# # import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = (time.strftime('%S'))
# print(timestamp)


#Exercise 

import time
timestamp = int(time.strftime('%H'))
print(timestamp)
if timestamp < 12 :
    print("Good Morning")
elif timestamp >12 and timestamp < 18 :
    print("Good Afternoon")
elif timestamp > 18 and timestamp < 24 :
    print("Good Evening")
else :
    print("cannot be executed")