'''* -> 0 or more occurnaces
+ -> 1 or more occurnaces
{3} -> Exact three occurences
{2,4} -> 2 and 4 occurnaces including 2 & 4
{2,}-> minimum 2 occurnaces
{,4}-> minimim 4 occurnaces'''

# import re

# data = "pyhton$testing life cycle"
# pattern = "\w+"
# result = re.findall(pattern , data)
# print(result)

# import re

# data = "234234%23234 23 "
# pattern = "\d*"
# result = re.findall(pattern , data)
# print(result)

# import re

# data = "234234%23234 23 "
# pattern = "\d{2,4}"
# result = re.findall(pattern , data)
# print(result)

import re

data = "234234%23234 23 "
pattern = "\d{2,}" # minimum 2 occurnaces
result = re.findall(pattern , data)
print(result)


import re

data = "234234%23234 23 "
pattern = "\d{,2}" # Maximum 2 occurnaces
result = re.findall(pattern , data)
print(result)


import re

data = "234234%23234 23"
pattern = "\d{3}" # Exact 3 occurnaces
result = re.findall(pattern , data)
print(result)