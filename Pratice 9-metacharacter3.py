# import re

# data = "Decs 14 15:56:34 2023-12-14T16:00:22Z core-rbi-logaggregator logaggregaor-7544b67647-vkhxn diksha@yahoo.com iuykj"
# pattern = r"logaggregat?or"

# match_list = re.findall(pattern, data)
# print(match_list)

#-----------------------------------------------------

# import re

# data = "Decs 14 15:56:34 123-456-7890 core-rbi-logaggregator logaggregaor- 7485962542 -vkhxn diksha@yahoo.com iuykj"
# pattern = r"\d{3}-?\d{3}-?\d{4}-?"

# match_list = re.findall(pattern, data)
# print(match_list)


#------------------------------------------------------
#check for valid URLS

# import re

# urls = ['https://www.cnn.com','http://www.youtube.com/watch','htttps://www.youtube.com/watch?v=TCWOwavqFrw']
# pattern = r"https?://\w+\.\w+\.\w+"

# for url in urls:
#     print(re.match(pattern,url))

#-------------------------------------------------------
    
# pipe sybmol | used to find two patterns parallay

import re

urls = ['https://www.cnn.com','http://www.youtube.com/watch','htttps://www.youtube.com/watch?v=TCWOwavqFrw', "9887987687"]
pattern = r"https?://\w+\.\w+\.\w+|\d+"

for url in urls:
    print(re.findall(pattern,url))
