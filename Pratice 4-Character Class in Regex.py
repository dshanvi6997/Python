# import re

# pattern = r'[0-9]'
# data = "Testing From Udemay courses which has total #100 section"

# match_list = re.findall(pattern, data)

# if match_list:
#     print("Charcter is defined :", match_list)
# else:
#     print("Charcter not defined")

#---------------------------------------------------------------------

# import re

# pattern = r'[a-z0-9A-Z]'
# data = "Testing From Udemay courses which has total #100 section"

# match_list = re.findall(pattern, data)

# print(match_list)

#------------------------------------------------------------------------

# import re

# pattern = r'[aeiou]'
# data = "Testing From Udemay courses which has total #100 section"

# match_list = re.findall(pattern, data)

# print(match_list)

#------------------------------------------------------------------------

# import re

# pattern = r'[#.]'
# data = "Testing From Udemay courses which has total #100.9 section"

# match_list = re.findall(pattern, data)
# print(match_list)

#------------------------------------------------------------------------

# import re

# pattern = r'[^A-Za-z]'    #carat symbol ^ it excludes the defined pattern
# data = "Testing From Udemay courses which has total #100.9 section"

# match_list = re.findall(pattern, data)
# print(match_list)

#------------------------------------------------------------------------

# Password should contain atleast one digit or one upper case

import re

Password = input("Enter the character : ")
pattern = r'[0-9A-Z]'    #carat symbol ^ it excludes the defined pattern
match_list = re.findall(pattern, Password)

if match_list:
    print("Valid Password :", match_list )
else:
    print("Not Found")    

