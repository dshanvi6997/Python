def num(a,b):
 print(f"{a} is greater then {b}") if a>b else print(f"{b} is greater then {a}") if a<b else print(f"{a} and {b} are equal")
a=int(input("ENter the value of a :"))
b=int(input("ENter the value of b :"))
num(a,b)

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 2
b = 330
print("A") if a > b else print("B")