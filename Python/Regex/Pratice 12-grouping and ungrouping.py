#Grouping 
# find username, domain, website type

# import re

# data= "Email IDs - durgeshsharma@gmail.eud, diksha@gmail.net, testing@gmail.com"
# pattern = r"(\w+)@(\w+)\.(\w+)"

# matchs = re.findall(pattern,data)

# for match in matchs:
#     print("Username :", match[0])
#     print("domain :", match[1])
#     if match[2] == 'eud':
#      print("Type is a : educational webiste:" )
#     elif  match[2] == 'net':
#        print("Type is a : Network webiste:" )
#     else:
#          print("Type is a : commerical webiste:" ) 
#     print("-------------")

#--------------------------------------------------------------------------------

#Non-Grouping : (?:www\.)?

import re

data= "URLs:- https://www.cnn.com, http://statnews.news, testing@gmail.com"
pattern = r"https?://(?:www\.)?\w+\.\w+"

matchs = re.findall(pattern,data)
print(matchs)