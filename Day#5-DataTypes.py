# Variables, DataTypes, Types of int : Int, float, complex
# Functions : int(), list(), Tuples(), dict(key:value pair)
# Types of print statment : sep(), end(), file()

a=3
b=3.2
c=True
d=complex(2,3)
e="Harry"

print(a)
print(b)
print(c)
print(d)
print(e)

print("type of a is", type(a))
print("type of b is", type(b))
print("type of c is", type(c))
print("type of d is", type(d))
print("type of e is", type(e))

listofstrings = ["apple", "banana", "mango", 1, 2.1, complex(2,3),["test1", "test2"]]
print(type(listofstrings))

tuples1 = (("test1", "test2"), ("test3", "test4"))
print(type(tuples1))

ok = { "name" : "durgesh", "Age": 28, "Job": "Quality Assurance", "boolean" : True}
print(type(ok))