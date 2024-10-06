# file= open("pratice.txt",'w') 
# lines =('Hi Everyone\n', 'We are learning File I/O\n', 'using java\n','I like programming in Java')
# file.writelines(lines)
# file.close()

# with  open("pratice.txt",'w') as file:
#  lines =('Hi Everyone\n', 'We are learning File I/O\n', 'using java\n','I like programming in Java')
#  file.writelines(lines)

# with  open("pratice.txt",'w') as file:
#  file.write('Hi Everyone\nWe are learning File I/O\nusing java\nI like programming in Java')
#  print(file)


#Write a function that replaces all word of Java with python

with open('pratice.txt', 'r') as f:
    original_text=f.read()

Updated_text=original_text.replace('java','pyhton')
    
with open('pratice.txt', 'w') as f:
    f.write(Updated_text)

print("Updated successfully")    

# Search if the file has word Learing or not

# with open('pratice.txt', 'r') as f:
#  for i in f.read().split():
#   if i == 'learning':
#    print("Yes")
#   else:
#    print("No")

# def find_word():
#  with open('pratice.txt', 'r') as f:
#   if 'learning' in f.read():
#    print("Yes there is a word learning in the prextice .txt file")
#   else:
#    print("No there is no such word call learning in the prextice .txt file") 
# find_word()

# WAF and find on which line does the word learning occur first

# def find_word_lines():
#   data=True
#   linenumer=1
#   with open('pratice.txt', 'r') as f:
#     while data:
#      data=f.readline()
#      if 'learning' in data:
#        print(linenumer)
#        return
#      linenumer+=1
#   return -1   
# find_word_lines()   

# From a file containing number seperated by comma, print the count() of even number
    
with open('number2.txt','w') as file:
    numbers=(12,23,14,15,12,3)
    file.write(",".join(map(str, numbers)))

count=0
with open("number2.txt",'r') as file:
 data = file.read()
 num = data.split(",")
 for i in num:
   if int(i) % 2 == 0:
     count+=1
print(count)     

  
