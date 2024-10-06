# Recursive function

# Factorial of a number

# factorial of 7 = 7*6*5*4*3*2*1
# facotrial of 1 = 1
# factorial of 0 = 1

# user defined number

def factorial(n):
 if n==0 or n==1 :
    return 1
 else :
   return  n * factorial(n-1)
n = int(input("Enter your number : ")) 
print(factorial(n))

#Pre-defined functions

def factorial(num): 
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1)) 
# Driver Code 
num = 1; 
print("Number: ",num)
print("Factorial: ",factorial(num))

if num == n:
   print('Correct')
else :
   print("Incorrect")




    
