# import re

# data = "Dec 14 15:56:34 robert.fitzgibbon.lab.go4labs.net  2023-12-14T16:00:22Z core-rbi-logaggregator-7544b67647-vkhxn 51.79.232.235:601[]"
# pattern = r"\d+"

# match_list = re.findall(pattern, data)
# print(match_list)


# import re

# data = "Dec 14 15:56:34 robert.fitzgibbon.lab.go4labs.net  2023-12-14T16:00:22Z core-rbi-logaggregator-7544b67647-vkhxn 51.79.232.235:601[]"
# pattern = r"\."

# match_list = re.findall(pattern, data)
# print(match_list)

#------------------------------------------------------------------
# import re

# data = "Dec 14 15:56:34 dikshasharma1@gmail.com 2023-12-14T16:00:22Z core-rbi-logaggregator-7544b67647-vkhxn diksha@yahoo.com"
# pattern = r"\w+@\w+\.\w+"

# match_list = re.findall(pattern, data)
# print(match_list)

#------------------------------------------------------------------
import re

data = "Dec 14 15:56:34 aaa bbb ababababa aaaabbbbbcb 2023-12-14T16:00:22Z core-rbi-logaggregator-7544b67647-vkhxn diksha@yahoo.com"
pattern = r"a*b+\w+"

match_list = re.findall(pattern, data)
print(match_list)

