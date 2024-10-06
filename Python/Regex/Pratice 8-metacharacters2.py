# import re

# data = "Decs 14 15:56:34 aaa bbb ababababa aaaabbbbbcb 2023-12-14T16:00:22Z core-rbi-logaggregator-7544b67647-vkhxn diksha@yahoo.com"
# pattern = r"^Dec"

# match_list = re.findall(pattern, data)
# print(match_list)

# import re

# data = "Decs 14 15:56:34 aaa bbb ababababa aaaabbbbbcb 2023-12-14T16:00:22Z core-rbi-logaggregator-7544b67647-vkhxn diksha@yahoo.com"
# pattern = r"[^a+]"

# match_list = re.findall(pattern, data)
# print(match_list)

import re

data = "Decs 14 15:56:34 aaa bbb ababababa aaaabbbbbcb 2023-12-14T16:00:22Z core-rbi-logaggregator-7544b67647-vkhxn diksha@yahoo.com iuykj"
pattern = r"\w+$"

match_list = re.findall(pattern, data)
print(match_list)


# if match_list:
#  print("Found :", match_list)
# else:
#  print("Not found")