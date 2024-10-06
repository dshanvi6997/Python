# import random
# import string
Suggestion = ["\nPlease do your selection if you want to Encode or Decode ?", "1. Encode", "2. Decode\n" ]
for i in Suggestion:
  print(i)
select = int(input("To select your choice enter 1 for Encode or enter 2 for decode :"))  
if select == 1:
  encode = input("Type your sentences want to Encode: ")
  start = 'qwe'
  end = 'ewq'
  # random_string = ''.join(random.choice(string.ascii_letters) for _ in range(3))
  sentence_split = encode.split()
  print(sentence_split)
  for i in sentence_split:
    if len(i)>=3:
      new_sentence = start + i[1:] + i[0] + end
      print( new_sentence, "" , end="")
    elif len(i)<3:
     new_sentence = i[::-1]
     print(new_sentence, "" ,end="")
else:
 decode = input("Type your sentences want to Decode : ")
 sentence_split = decode.split()
 for i in sentence_split:
    if len(i)>=3:
      new_sentence = i[-4] + i[3:-4]
      print( new_sentence, "" , end="")
    elif len(i)<3:
     new_sentence = i[::-1]
     print(new_sentence, "" ,end="")