fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
print(x) 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

list = [1,2,3,4,5,6,7,8,9]
for num in list:
    if num == 7:
        break
#     print(num)

list = [1,2,3,4,5,6,7,8,9]
for num in list:
    if num == 7:
        continue
    print(num)    


num = int(input("enter the number :"))
for i in range(12):
    if i==0:
        continue
    print(num ,'*', i , "=" , num*i)

num = int(input("enter the number :"))
for i in range(12):
    if i==7:
        break
    print(num ,'*', i , "=" , num*i)    

i = 1
while i < 6:
  print(i)
  if i ==5:
    break
  i +=1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)