# import re

# pattern = r'\d'
# data = "testing status life cycle100"

# match_filter = re.finditer(pattern, data)

# for match in match_filter:
#     print("Found :", match.group())
# else:
#     print("Not Found")
# #_____________________________________________________________
# import re

# pattern = r'\D'
# data = "testing status life cycle100"

# match_filter = re.finditer(pattern, data)

# for match in match_filter:
#     print(match.start(),"-->",match.group(),end=" ")
# else:
#     print("Not Found")    

# #_____________________________________________________________
# import re

# pattern = r'\w'
# data = "testing status life-cycle 100"

# match_filter = re.finditer(pattern, data)

# for match in match_filter:
#     print(match.start(),"-->",match.group(),end=" ")
# else:
#     print("Not Found")

# #_____________________________________________________________
# import re

# pattern = r'\W'
# data = "testing status life-cycle $100"

# match_filter = re.finditer(pattern, data)

# for match in match_filter:
#     print(match.start(),"-->",match.group(),end=" ")
# else:
#     print("Not Found")

#_____________________________________________________________
# import re

# pattern = r'\s'
# data = "testing status life-cycle $100"

# match_filter = re.finditer(pattern, data)

# for match in match_filter:
#     print(match.start(),"-->",match.group(),end=" ")
# else:
#     print("Not Found")

# #_____________________________________________________________
# import re

# pattern = r'\S'
# data = "testing status life-cycle $100"

# match_filter = re.finditer(pattern, data)

# for match in match_filter:
#     print(match.start(),"-->",match.group(),end=" ")
# else:
#     print("Not Found")  
  
# #_____________________________________________________________
# import re

# pattern = r'\bstatus\b'
# data = "testing status life-cycle $100"

# match_filter = re.finditer(pattern, data)

# for match in match_filter:
#     print(match.start(),"-->",match.group(),end=" ")

    #_____________________________________________________________
# import re

# pattern = r'\bstatus\b'
# data = "testing status life-cycle $100"

# match_filter = re.finditer(pattern, data)

# for match in match_filter:
#     print(match.start(),"-->",match.group(),end=" ")

#_____________________________________________________________
# import re

# pattern = r'\bstatus\b'
# data = "testing status life-cycle $100"

# match_filter = re.finditer(pattern, data)

# for match in match_filter:
#     print(match.start(),"-->",match.group(),end=" ")    

#_____________________________________________________________
# import re

# pattern = r'\Atesting'
# data = "testing status life-cycle $100"

# match_filter = re.finditer(pattern, data)

# for match in match_filter:
#     print(match.start(),"-->",match.group(),end=" ")       

#_____________________________________________________________
# import re

# pattern = r'e\Z'
# data = "testing status life-cycle $100"

# match_filter = re.finditer(pattern, data)

# for match in match_filter:
#     print(match.start(),"-->",match.group(),end=" ")    

import re

pattern = r'.'
data = "testing status life-cycle $100"

match_filter = re.finditer(pattern, data)

for match in match_filter:
    print(match.start(),"-->",match.group(),end=" ")     