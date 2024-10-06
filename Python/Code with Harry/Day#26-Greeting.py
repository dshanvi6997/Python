
time = int(input("ENter time :"))
meridiem = input("enter meridiem :")

# if time >= 7 and time < 12 and meridiem == 'AM' :
#     print("Hey, Good morning")
# if time==12 and meridiem == "PM" :
#      print("Hey, Good Afternoon")
# elif time >1 and time <4 and meridiem == "PM" :
#      print("Hey, Good Afternoon")
# elif time> 4 and time <12 and meridiem =="PM":
#        print("Hey, Good Evening")
# elif time==12 and meridiem == "AM" :
#      print("Hey, Good Night")
# else :
#  print("Not a valid input")
# else :
# print("not a valid number")
    

if time >=1 and time < 12 and meridiem == 'AM' :
    print("Hey, Good morning")
# if time >= 7 and time < 12 and meridiem == 'AM' :
#     print("Hey, Good morning")
elif time==12 and meridiem == "PM" :
     print("Hey, Good Afternoon")
elif time >1 and time <4 and meridiem == "PM" :
     print("Hey, Good Afternoon")
elif time> 4 and time <12 and meridiem =="PM":
       print("Hey, Good Evening")
elif time==12 and meridiem == "AM" :
     print("Hey, Good Night")
else :
     print("Not a valid input")
