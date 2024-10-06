'''Determines the largest or smallest number among the three, or checks if they are all equal. Below are a few different 
examples for comparing three numbers:'''

def Aramethic_operations(a,b,c) :

 if a == b == c:
    print("All three numbers are equal")
 else:
    if a>b:
        if a>c:
            print("a is greater")
        else:
            print("c is greater") 
    else :
        if b>c :
            print("b is greater") 
        else :
            print("c is greater")   

    if a<b:
        if a<c:
            print("a is smaller")
        else:
            print("c is smaller") 
    else :
        if b<c :
            print("b is smaller") 
        else :
            print("c is smaller") 

a = float(input("Please enter 1st numbers :"))
b = float(input("Please enter 2nd numbers :"))
c = float(input("Please enter 3rd numbers :"))                            

Aramethic_operations(a,b,c)



# number = 5

# # outer if statement
# if number >= 0:
#     # inner if statement
#     if number == 0:
#       print('Number is 0')
    
#     # inner else statement
#     else:
#         print('Number is positive')

# # outer else statement
# else:
#     print('Number is negative')