# # String
# str1 = "name"
# print(str1)

# # Multiline string can be enclosed iwth double and single inverted commas
# str2 = """str1
# str2
# str3
# str4"""
# print(str2)

# accesing character or string

# name = 'Durgesh'
# print(name[-7])  # Negative counts number from end
# print(name[3])   # Postive counts number from start
# print(name[2])

# Loops in Stings

# prof =  "Quality Assurnace"
# for completesrting in prof:
# print(completesrting)

#Slicing
# In Python, string slicing is done using the syntax string[start:end], where:
# start is the index where the slice starts (inclusive).
# end is the index where the slice ends (exclusive).

# country = 'Landon   3877658'
# print(country)
# print(country[-1:])  # n
# print(country[0:])   # Start from 0 and print till end
# print(country[0:1])  # 0 : n-1
# print(country[0:10]) # 0 : n-1
# print(country[2:4])  # n and d
# # print(country[-4:-3])  # Python slices from the start to end index moving left to right, and an empty string is returned if the start index is logically after the end index.
# country1 = 'Landon   3877658'
# # print(country1[-5:-3])  # -7 = 7 and 5-3 = start from the same character ie 77
# print(country1[0:-2]) # 0 index is L and n-1 = -2-1 = -3 = 6 -> Landon   38776

#Questions 1

# string = 'string slicing'
# print(string[2:10:2])   

# Ans - rn 
# Applying the Slice string[2:10:2]:

# Starting at index 2: The character here is 'r'.
# Ending before index 10: The character at index 10 is 'c', but it is not included.
# Step of 2: This selects every second character from the start index up to but not including the end index.
# Characters Selected:
# Index 2: 'r'
# Index 4: 'n'
# Index 6: ' ' (space)
# Index 8: 'l'


#Questions 2

string = 'string slicing'
print(string[::-2]) 
# print(string[4::2]) 

# Breaking Down string[4::2]:

# start = 4: The slice starts at index 4 (inclusive).
# end is not specified: The slice goes until the end of the string.
# step = 2: This means every second character starting from index 4 will be selected.






