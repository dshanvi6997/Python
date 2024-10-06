# sentence = (" I love to read book name {1} and i have already on through total {0} books so far")

# book = ('Rich Dad Poor Dad', 'Future does exist')
# count = (5,4)

# # print(sentence.format(book, count))
# # print(sentence.format(book[1], count))
# print(sentence.format(count[1], book[1]))

# print(f"I love to read book name {book[0]} and i have already on through total {count} books so far")

# string = ("currently i have total {}")
# money = 354000.3245
# print(string.format(money))
# print(f"currently i have total {money}")
# print(f"currently i have total {money:.3f}")


# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))

num = 3.14159
print(f"{num:.2f}")


# # Addition of two number  :

print(f"{2*3}")
print(f"{{2*3}}")

int = [1,4,7]
print(f"{int[1]+int[0]+int[2]}")

int1={'a':90,'b':90}
print(f"{int1['a']+int1['b']}")

a=1
b=2
c=3
print(f"{a+b+c}")

import datetime

today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")

