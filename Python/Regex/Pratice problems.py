#Data Validation
# import re

# data = input("Enter Email ID :")
# pattern = r"^[a-zA-Z_][\w+_\.]+@[a-zA-Z]+\.\w+"

# match = re.match(pattern,data)
# if match:
#     print("Valid Email ID")
# else:
#     print("Invalid Email ID")

#Data Cleaning

# import re

# data = input("Enter Character :")
# pattern = r"\s+"   
# data=data.strip()
# match = re.sub(pattern," ",data)
# print(match)


# with open('mytextfile.txt','w') as file:
#  text=file.write("87676987 8769868")

# Data searching into the file

with open('mytextfile.txt','r') as file:
 text=file.read()

import re 
pattern = r'\d{2,9}'
match = re.findall(pattern, text)
print(match)

