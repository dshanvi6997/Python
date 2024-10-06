'''In this example we will ask the user to enter a value between 1 and 6. Then using the match case with OR operator 
we have clubbed the pairs one 1 case each which will display its corresponding number in words.'''

# number = int(input("Enter a value betweeen 1 and 6 : "))

# match number:
#  case 1|2:
#   print("ane or Two")
#  case 3|4:
#   print("three or four")
#  case _:
#   print("Invalid number")


'''Example: In this example we are using a python list for pattern matching. We are matching the first element of the lost and also 
used positional arguments to match the rest of the list.'''
   
num = int(input("Enter a number: "))
    
    # match case
match num:
        # pattern 1
    case num if num > 0:
            print("Positive")
        # pattern 2
    case num if num < 0:
            print("Negative")
        # default pattern
    case _:
            print("Zero")