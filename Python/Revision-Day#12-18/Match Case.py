'''Example: In this example we will ask the user to enter a value between 1 and 3 and display its corresponding number in words 
# using the simple match case statement'''

number = int(input("Enter a number between 1 and 3 :"))
match number :
 case 0 :
    print("Case 1 matched")
 case 1 :
    if number > 10 :
     print(number, "is matched is case 1")
    else :
     print(number, "is matched in case 1")
 case 2 if number > 1 and number < 3 :
    print(number, "is matched is case 2")
 case _ :
    print("Out of the loop")

'''Example: In this example we will ask the user to enter a value between 1 and 6. Then using the match case with OR operator 
      we have clubbed the pairs one, 1 case each which will display its corresponding number in words.'''

number = int(input("Enter a number between 1 and 6 :"))
match number :
   case 1 | 2 :
    print (number, "number is one or TWO")
   case 3 | 4 :
    print (number, "number is Three or FOUR")
   case 5 | 6 :
    print (number, "number is FIVE or SIX")
   case _ : 
    print("Out of the Loop")

'''Example: In this example, we will use if condition along with match case statement to check if a number entered by the 
user is positive, negative or zero'''

num = int(input("Enter a number which consist postive, negative and a zero value :"))
match num :
  case num if num > 0 :
    print (num, "is a postitve number")
  case num if num < 0 :
    print (num, "is a negative number")
  case num if num == 0 :
    print (num, "doesn't give any value")
  case _ : 
    print("Out of the Loop")


'''Example: In this example, we are using a python string to check if a character is present in the string or not using match case.
We provide the string along with the index of the character we want to check for in the string to the match case. Then we defined
the match cases as to what that character might be'''

str1 = "durgesh"

match (str1[1]) :
    case "u" :
        print("Letter u is present in the character")
    case "h" :
        print("Letter h is present in the character")
    case _ : 
     print("Out of the Loop")


























