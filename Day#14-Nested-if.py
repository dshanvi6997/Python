num =int(input("Please neter your number :"))

if num<0:
   print("number is negative :", num)
elif num>0:
     print("number is between 0-10 :", num)
     if num >=10 and num <=20:
      print('number is between 10-20 :' , num)
     else :
      print('number is greater than 20 :', num)
else :
     print("number is zero")