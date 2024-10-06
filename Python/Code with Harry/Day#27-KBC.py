# questions = ["How many Days in a week ?", "How many days in a month of dec ?"]
# ans = [7,31,2,5]

# print(questions[0])
# print("1. 7", " \n2. 31", " \n3. 4", " \n4. 6")
# answer = int(input("My Ans is :"))

# for i in range(1):
#  if answer == 7 :
#     print("Correct, You earned 5 points")
#     print(questions[1])
#     print("1. 7", " \n2. 31", " \n3. 4", " \n4. 6")
#     answer = int(input("My Ans is :"))
#     if answer == 31 :
#       print("Correct, You earned 10 points")
#     else :
#        print('Wrong ans')
#  else :
#    print('Wrong ans')

print("Tho chalie shuru karte hai kon banega cororpati\n")
Question = [
"1. Current Railway Minister of India is ?\n",
"2. Which god is also known as ‘Gauri Nandan’?\n",
"3. Which city is known as the Pink City of India?\n"
]
Options = [
"\nA. Mamta Banarjee \nB. Ram Vilash \nC. Ashwini Vaishnaw \nD. Piyush Goyal\n",
"\nA. Agni \nB. Indra \nC. Hanuman \nD. Ganesh\n",
"\nA. Banglore \nB. Maysore \nC. Jaipur \nD. Kochi\n"
]
Answers = ['C', 'D', 'C']
pricemoney = [0,1000,2000,3000]

print(Question[0], Options[0])
i = input("Kis answer ko lock kiya jaye ?: ")
if i == Answers[0]:
      print("Shai Jawab aapne jeeta hai", pricemoney[1] , "Rupyee badte hai dusre sawal par\n")
      print(Question[1], Options[1])
      i = input("Kis answer ko lock kiya jaye ?: ")

      if i == Answers[1]:
       print("Shai Jawab aapne jeeta hai", pricemoney[2] , "Rupyee badte hai tesre sawal par\n")
       print(Question[2], Options[2])
       i = input("Kis answer ko lock kiya jaye ?: ")
      
       if i == Answers[2]:
         print("Congrulations Shai Jawab aapne jeeta hai", pricemoney[3] , "aap itne dhan rashi ka kya karoge??\n")
       else: 
         print(f"Galat Jawab!! Shai jawab hai C. Jaipur")
      else: 
       print(f"Galat Jawab!! Shai jawab hai D. Ganesh")
else: 
       print(f"Galat Jawab!! Shai jawab hai C. Ashwini Vaishnaw")
