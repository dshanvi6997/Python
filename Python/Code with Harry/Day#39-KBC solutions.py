
print("Tho chalie shuru karte hai kon banega cororpati\n")
Questions = [
[
"1. How is the Current Railway Minister of India is?\n","A. Mamta Banarjee", "\nB. Ram Vilash \n","C. Ashwini Vaishnaw","\nD. Piyush Goyal\n","C"
    ],
[
"2. Which god is also known as ‘Gauri Nandan’?\n", "\nA. Agni", "\nB. Indra" , "\nC. Hanuman", "\nD. Ganesh\n", "D"
    ],
[
"3. Which city is known as the Pink City of India?\n", "\nA. Banglore",  "\nB. Maysore",  "\nC. Jaipur",  "\nD. Kochi\n", "C"
    ],
]
Money=[0,100,200,300]
for i in range(0,len(Questions)):
    Question = Questions[i]
    print(f"Ye raha aapka phala sawal {Money[i+1]} k liye aapke screen par\n",Question[0])
    print(f"{Question[1]} , {Question[2]} , {Question[3]} , {Question[4]}")
    Ans = input("Enter you Answer between A-D : ")
    if Ans == Question[-1]:
      print(f"You Won {Money[i+1]}")
    else :
        print(f"Losser you will take back home {Money[i]} Rupye")
        break 
    
    
  


    























# print(Question[0], Options[0])
# i = input("Kis answer ko lock kiya jaye ?: ")
# if i == Answers[0]:
#       print("Shai Jawab aapne jeeta hai", pricemoney[1] , "Rupyee badte hai dusre sawal par\n")
#       print(Question[1], Options[1])
#       i = input("Kis answer ko lock kiya jaye ?: ")

#       if i == Answers[1]:
#        print("Shai Jawab aapne jeeta hai", pricemoney[2] , "Rupyee badte hai tesre sawal par\n")
#        print(Question[2], Options[2])
#        i = input("Kis answer ko lock kiya jaye ?: ")
      
#        if i == Answers[2]:
#          print("Congrulations Shai Jawab aapne jeeta hai", pricemoney[3] , "aap itne dhan rashi ka kya karoge??\n")
#        else: 
#          print(f"Galat Jawab!! Shai jawab hai C. Jaipur")
#       else: 
#        print(f"Galat Jawab!! Shai jawab hai D. Ganesh")
# else: 
#        print(f"Galat Jawab!! Shai jawab hai C. Ashwini Vaishnaw")
