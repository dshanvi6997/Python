"""for loop  : for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but 
# iterating over strings, lists, tuples, sets and dictionaries."""

# name = 'Abhishek'
# for i in name:
#     print(i, end=", ")

# colors = ["Red", "Green", "Blue", "Yellow"]
# for x in colors:
#     print(x)

# colors = ("Red", "Green", "Blue", "Yellow")
# for x in colors:
#     print(x)

# colors = ("Red:r1", "Green:g1", "Blue", "Yellow:y1")
# for x in colors:
#     print(x)  
#     for x1 in x:
#         print(x1) 

#Range () - What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?

for number in range(1,10,2):
    print(number)
for number in range(1,10,):
    print(number)
