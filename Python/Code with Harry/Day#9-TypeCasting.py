# Type Casting - Conversion of one data type into another datatype
# Explict and Implicit Type Casting
# Explicit Typecasting is something which is done by enduser

# Python Convert string to int
a = "5"
b = "6"
print((int(a)+int(b)))
print(type(int(a)+int(b)))  # Converting string datatype into integer datatype

# Python Convert Int to Float
c= 2
d= 3
print(float(c-d))
print(type(float(c-d)))

# Python Convert Float to Int 
e= 1232.234
f= 312.3
print(int(e)*int(f))
print(type(int(e)*int(f)))

# Python Convert int to String 
g = 90
h= str(90)
print(str(h))
print(type(str(h)))

# Python Convert String to float
i= "9"
j= float(i)
print(type(j))
print(j)

# Addition of string and integer Using Explicit Conversion
k="789"
l=123
print(int(k)+l)
print(type(int(k)+l))

# Implicit TypeCasting is something which is done bydefault by python
c = 987.2
d = 6
print(type(c+d))
print(c+d)