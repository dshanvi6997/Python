# 1. Write a Python program to sum all the items in a list.

# number = [12,123,12,12]
# sum=0
# for i in number:
#     sum = sum + i
# print(sum)   


#3. Write a Python program to get the largest number from a list.

# number = [12,123,12,134]
# max=number[0]
# for i in number:
#     if i>max:
#         max=i
# print(max) 

'''Write a Python program to convert a list of multiple integers into a single integer'''
#Sample list: [11, 33, 50]
#Expected Output: 113350

# list = [11, 33, 50]
# result= "".join(map(str, list))
# print(result)

#Write a Python program to select the odd items from a list.

# list =[1,2,3,4,5,6,7,8,9]
# print(list[::2])

#Write a Python program to select the even items from a list.

# list =[12,23,45,76]
# even=set()
# for i in list:
#     if i %2 == 0:
#         even.add(i)
# print(even)  

list3 =[1,2,3,4,5,6,7,8,9,1,2,3,4,5]
new_list=set(list3)
print(new_list)
list1= list(new_list)
print(list1)

