# f=open("mytextfile.txt", "r")
# text=f.read()
# print(text)
# f.close()

# f=open("mytextfile.txt", "r")
# text=f.read(3)
# print(text)
# f.close()

# f=open("mytextfile.txt", "r")
# line1=f.readline()
# print(line1)
# line2=f.readline()
# print(line2)
# f.close()

# f=open("mytextfile.txt", "r")
# text=f.read()
# print(text)
# line1=f.readline()
# print(line1)
# line2=f.readline()
# print(type(line2))
# print(line2)
# f.close()

f=open("mytextfile.txt", "r+")
f.write("hello")
print(f.read())
