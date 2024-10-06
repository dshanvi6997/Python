# file=open('mytextfile.txt','r')
# text=file.read()
# print(text)
# file.close()


# file=open('mytextfile.txt','wt')
# file.write("Hey Hellow how are you!!..")
# file.close()


# file=open('mytextfile.txt','at')
# file.write("Hey Hello how are you!!..")
# file.close()

# file=open('mytextfile.txt','x')
# file.write("Hey Hello how are you!!..")
# file.close()


# with open('mytextfile.txt','r') as file:
#  text=file.read()
# print(text)


# with open('mytextfile.txt','w') as file:
#  file.write("Hey durgesh how are you!!..")

# with open('mytextfile.txt','a') as file:
#  file.write("Hey diksha how are you!!..")

# import os
# os.remove("number.txt")

with open('number.txt','w') as file:
    num=[12,34,45,56,14]
    file.write(",".join(map(str, num)))

count=0
with open('number.txt','r') as file:
 data=file.read()
 for i in data.split(","):
#   print(i)
  if int(i) %2 == 0 :
    count+=1
print(count)


    