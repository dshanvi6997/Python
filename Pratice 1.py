import re

pattern = "[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]+)?([Zz]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?"
text = 'Dec 14 15:50:07 robert.fitzgibbon.lab.go4labs.net  2021-12-14T15:53:56Z core-rbi-logaggregator-7544b67647-vkhxn 51.79.232.235:601[1]: {"action":"user.add","assignedGroups":"[]","assignedRoles":"[User Admin]","correlationId":"26e20792-f126-4b45-a409-86221c78a090","eventCode":"Key_ActionComplete","eventType":"Key_Success","level":"info","message":"New user added.","newUserId":"b1450fc9-0242-4dbc-9a75-71eca50709d4","newUsername":"user2@fp.com","service":"Security","tenantId":"3a19ba0b-60a8-4191-b85b-70d407fe42c7","tenantName":"Rbi-tenant","time":"2023-12-14T15:53:57Z","userDisplayName":"rohan","userId":"1d740e21-31ae-46c9-a32c-4b32f8afb17d","username":"rn@fp.com"}'

match = re.search(pattern, text)
print(match)

