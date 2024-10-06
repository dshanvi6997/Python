#Find word 'Python'

# import re

# pattern = "pyhton"
# data = "pyhton testing life cycle"

# result = re.search(pattern , data)
# print(result)
# print(type(result))

# if result:
#  print(f"Found : {result.group()}")  # Grouping
# else:
#  print("not found") 

# Flags Case Sensitive -----------------------------------------------------------------------------------------

# import re

# pattern = r"pyhton"                     # raw string
# data = "PYTHON testing life cycle"

# result = re.search(pattern , data, re.IGNORECASE)   # Flags Case
# print(result)
# print(type(result))

# if result:
#  print(f"Found : {result.group()}")
# else:
#  print("not found")

#-----------------------------match()-----------------------------------------------

# import re

# pattern = r"PYthon"                     # raw string
# data = "hello, PYTHON testing life cycle"

# result = re.match(pattern , data, re.IGNORECASE)   # match function used to find the word at the start it self
# print(result)
# print(type(result))

# if result:
#  print(f"Found : {result.group()}")
# else:
#  print("not found")


#----------------------------- compile

#regular expression object  : re.compile(pattern, flags)

import re

pattern = re.compile("hello",re.IGNORECASE)   #compile function
print(type(pattern))
data = "hello, PYTHON testing life cycle"

result = re.match(pattern , data)   # match function used to find the word at the start it self
print(result)
print(type(result))

if result:
 print(f"Found : {result.group()}")
else:
 print("not found")

 