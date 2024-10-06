import re

data = "Dec 14 15:56:34 robert.fitzgibbon.lab.go4labs.net  2023-12-14T16:00:22Z core-rbi-logagg\wregator-7544b67647-vkhxn 51.79.232.235:601[1]"
pattern = r"\\w"

match_filter = re.finditer(pattern, data)

for match in match_filter:
 print(match)

#--------------------------------------------------

# import re

# data = "Dec 14 15:56:34 robert.fitzgibbon.lab.go4labs.net  2023-12-14T16:00:22Z core-rbi-logaggregator-7544b67647-vkhxn 51.79.232.235:601[]"
# pattern = r"\[\]"

# match_filter = re.finditer(pattern, data)

# for match in match_filter:
#  print(match)