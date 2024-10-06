info = (1,2,3,4,5)
for i in info:
    print(i)
else:
    print("loop completed")   

info = {'name':'Karan', 'age':19, 'eligible':True, 'Non-eligible':False}
for i in info.values():
    print(i)
else:
    print("loop completed")


info = [1,2,3,4,5]
for i in info:
    print(i)
else:
    print("loop completed")


for i in range(2,4):
    print(i)
else:
    print("loop completed")

i=0
while i<5:
    print(i)
    i = i+1
else:
    print(f"loop completed and last number is {i}")
