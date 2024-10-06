'''Example: In this example we will ask the user to enter a value between 1 and 3 and display its corresponding number 
in words using the simple match case statement.'''

num = int(input("Please enter a value betwenn 1 and 3 :"))
match num:
    case _ if num >1 and num <3 :
     print(num, 'in words can be written as THREE')
    case _ :
     print('not a vaid number') 

#https://www.geeksforgeeks.org/python-match-case-statement/


'''In this example, we will use if condition along with match case statement to check if a number entered 
bt the user id positive, negative or zero.'''

'''In this example, we are using a python string to check if a character is present in the string or not using match case. 
We provide the string along with the index of the character we want to check for in the string to the match case. Then we defined the 
match cases as to what that character might be. '''

