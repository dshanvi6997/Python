name = input("enter string :")
if len(name)>3 and 'ing' in name:
  newname1 = name.replace(name, name+'ly')
  print(newname1)
elif len(name)<3:
 print(name)
elif len(name)>3 and 'ing' not in name:
  newname1 = name.replace(name, name+'ing')
  print(newname1)

  