''''
variable.update(variable)
variable.update({"key:value"})
variable.clear()
variable.pop()
variable.popitem()
del variable
del variable['key']'''



info = {100:'kiran',101:'durgesh',102:'shetty'} 
info1 = {103:'kiran','eligible':True, 'name':'shetty'} 

info.update({101:'sagar'})
print(info)

info.update(info1)
print(info)

# Remove list form the dict

info.clear()
print(info)

# pop remove mentioned key:value pair

info.pop(101)
print(info)

# popitem remove last key value pair

info.popitem()
print(info)

# delete dict

del info
print(info)

del info1['eligible']
print(info1)





