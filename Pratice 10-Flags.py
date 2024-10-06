# import re

# data = "Decs 14 15:56:34 123-456-7890 core-rbi-Logaggregator Logaggregaor- 7485962542 -vkhxn diksha@yahoo.com iuykj"
# pattern = r"logaggregator"

# match_list = re.findall(pattern, data,re.IGNORECASE)
# print(match_list)

#-------------------------------------------------------------------------------------

# import re

# data = '''Decs 14 15:56:34 123-456-7890 core-rbi-Logaggregator Logaggregaor- 7485962542
# 15:56:34 123-456-7890 core-rbi-Logaggregator Logaggregaor- 74859625465
# 15:56:34 123-456-7890 core-rbi-Logaggregator Logaggregaor- 742542'''
# pattern = r"\d+$"

# match_list = re.findall(pattern, data,re.MULTILINE)
# print(match_list)

#-----------------------------------

# import re

# data = '''Decs 14 15:56:34 123-456-7890 cor\ne-rbi-Logaggr\wegator Logagg\dregaor- 7485962542'''

# pattern = r"."

# match_list = re.findall(pattern, data,re.DOTALL)  
# print(match_list)


# import re

# data = '''Decs 14 15:56:34 123-456-7890 cor\ne-rbi-Logaggr\wegator Logagg\dregaor- 7485962542'''

# pattern = r"."

# match_list = re.findall(pattern, data,re.S)  
# print(match_list)


#_------------------------------------------------------------------


# import re

# data = "Dec 14 15:56:34 dikshasharma1@gmail.com 2023-12-14T16:00:22Z core-rbi-logaggregator-7544b67647-vkhxn diksha@yahoo.com"
# pattern = r'''\w+
# @\w+
# \. # to detect dot
# \w+ #comment '''

# match_list = re.findall(pattern, data, re.VERBOSE)
# print(match_list)


# import re

# data = "Dec 14 15:56:34 dikshasharma1@gmail.com 2023-12-14T16:00:22Z core-rbi-logaggregator-7544b67647-vkhxn diksha@yahoo.com"
# pattern = r'''\w+
# @\w+
# \. # to detect dot
# \w+ #comment '''

# match_list = re.findall(pattern, data, re.X)
# print(match_list)


#------------------------------------------------------------------------------------

import re

data = "¥ ¤ tell how "
pattern = r"\b\w+\b"

match_filter = re.findall(pattern, data, re.ASCII )

for match in match_filter:
 print(match)

import re

data = "¥ ¤ tell how "
pattern = r"\b\w+\b"

match_filter = re.findall(pattern, data, re.A )

for match in match_filter:
 print(match)