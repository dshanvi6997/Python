# with open('pratice.txt', 'w') as f:
#  f.write('Helloworld123 123')

# with open('pratice.txt', 'r') as f:
#  f.seek(3)
#  print(f.tell())
#  print(f.read(5))
#  print(f.truncate(5))


with open('sample.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5)

with open('sample.txt', 'r') as f:
  print(f.read())


  







