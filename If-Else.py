# Short hand If you have only one statement to execute, you can put it on the same line as the if statement.

a= 1
b =2
if a > b : print("a is greater than b")

# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

print (a) if a>b else print(b)

#You can also have multiple else statements on the same line:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#https://github.com/aisha-batool/Python-Practice-Exercises/blob/master/5-%20IF%2C%20ELSE%20AND%20ELSE%20IF%20STATEMENTS%2C%20TESTING%20SET%20OF%20CONDITIONS.pdf

"""Write a program that prompts the user for their name, and then displays a special greeting to that person if their name 
is the same as yours. If the name entered by the user is anything other than your name, your code should not produce any output"""

name = input("Please enter your name :")
if name == "Durgesh" :
    print("Hey same is my name")
else :
    print("Sorry!! Please move on")

'''Write a program that takes a calendar year in YYYY format in a variable. Check & notify the user whether it is a leap year or not.'''

leapyear = int(input("enter a Year :"))
if  leapyear % 400 == 0 and leapyear % 100 == 0 :
    print("Hey Year is leap Year")
elif  leapyear % 4 == 0 and leapyear % 100 != 0 :
    print("Hey Year is leap Year")
else:
    print("Year is not a leap year")

'''Write a program that takes a character (i.e. string of length 1) and returns true if it is a vowel, false otherwise.'''

x = input("Enter a character :")
if (x== 'a' or x=='e' or x=='i' or x=='o' or x=='u' or x=='A' or x=='E' or x=='I' or x=='O' or x=="U") :
    print("Entered charactered is vowel")
else:
    print("Not a vowel")


x = input("Enter a vowel :")
if (x== 'a' or x=='e' or x=='i' or x=='o' or x=='u' or x=='A' or x=='E' or x=='I' or x=='O' or x=="U") :
  print("it is a vowel")
else:
    print("Not a vowel")

    



