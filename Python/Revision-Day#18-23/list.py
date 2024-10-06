# # Check whether an item in present in the list?

# list=['apple','grapes','orange']
# print(list)
# if 'apple' in list :
#  print("yes present")
# else :
#  print("not present")

# if 'ape' in 'grapes' :
#  print("yes present")
# else :
#  print("not present")

# #Range of Index:

# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[3:7])	#using positive indexes
# print(animals[-7:-2])	#using negative indexes'

# #List Comprehension

# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# animals_a = [item for item in animals if 'on' in item]
# print(animals_a)

# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# animals_a = [item for item in animals if (len(item) > 4)]
# print(animals_a)



# '''Write a program that takes a character (i.e. string of length 1) and returns true if it is a vowel, false otherwise.'''

# x = input("Enter a character :")
# if (x== 'a' or x=='e' or x=='i' or x=='o' or x=='u' or x=='A' or x=='E' or x=='I' or x=='O' or x=="U") :
#     print("Entered charactered is vowel")
# else:
#     print("Not a vowel")


# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  # List of vowels (both lowercase and uppercase)
# char = input("Enter a character: ")
# for char in vowels:
#   if len(char) == 1:
#     if new==vowels:
#         print(f"{char} is a vowel.")
#     else:
#         print(f"{char} is not a vowel.")
#   else:
#     print("Please enter a single character.")

# def is_vowel(character):
#     """Check if a character is a vowel using a list."""
#     vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  # List of vowels (both lowercase and uppercase)
    
#     if character in vowels:
#         return True
#     else:
#         return False

# # Input from user
# char = input("Enter a character: ")

# # Check if the input is a single character
# if len(char) == 1:
#     if is_vowel(char):
#         print(f"{char} is a vowel.")
#     else:
#         print(f"{char} is not a vowel.")
# else:
#     print("Please enter a single character.")


# username = ["Durgeshsharma", "Sagarsharma", "vinodsahrma","vinod"]

# for name in username :
#     if len(name)>10:
#         print(name, "has more than 10 character")
#     else:
#         print(name ,"has less than 8 character")


username = ["Durgeshsharma", "Sagarsharma", "vinodsahrma","vinod"]

for name in username :
    if len(name)>10:
        print(name, "has more than 10 character")
    


        















