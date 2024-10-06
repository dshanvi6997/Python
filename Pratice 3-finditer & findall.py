# re.finditer()
# re.findall()

# import re

# pattern = re.compile("test", re.IGNORECASE)
# data = "testing the test filetest"
# match=re.findall(pattern, data)
# count = 0
# for data in match:
#     count +=1
#     print(match)
# print(count)  

#---------------------------------------------------------------------

# import re

# pattern = re.compile("test", re.IGNORECASE)
# data = "testingtest the test filetest"
# match_iter=re.finditer(pattern, data)
# count = 0
# for match in match_iter:
#  count +=1
#  print(match)
# print(count)

#---------------------------------------------------------------------
import re

pattern = re.compile("test", re.IGNORECASE)
data = "testingtest the test filetest"
match_iter=re.finditer(pattern, data)
count = 0
for match in match_iter:
 count +=1
 print(f"{match.group()}, {match.start()}, {match.end()}")
print(count)


    