# # Strings methods 

# # upper() - convert the letter in upper case
name= 'durgesh sharma'
print(name.upper())

# # # lower() - convert the letter in upper case
name= 'DURGESH123 SHARMA456'
print(name.lower())

# # # len() - convert the letter in upper case
name = 'durgesh sharma is a good boy'
length = len(name)
print(length)

# # rstrip() - remove the trailling character
name = 'durgesh sharma is a good boyyyyyyyyyy?'
print(name.rstrip("boy?"))

# # #split() - It will split the string into required character
name = 'durgesh sharma is a good boy'
print(name.split('is'))

# #replace() - Replace all occurnace of a string with a new string
name = 'durgesh sharma is a good boy'
print(name.replace('a', 'aaaa'))
print(name.replace('sharma','diksha'))

# #capitalize() - Conver the first letter in upper case and rest all letters under lower case
name = 'durgesh shARma Is a gOod boY?'
print(name.capitalize())

# # center() - used to align the strings
name = 'durgesh shARma Is a gOod boY?'
name1 = name.center(40,"=")
print(name1.capitalize())

# #Count() - Gives the count of any particualr character
name = 'durgesh shARma Is a gOod boY?'
print(name.count('P'))

# #endswitch() - Check if the string is ending with any prticular character
name = 'durgesh shARma Is a gOod boY?'
print(name.endswith('boY?'))
print(name.endswith('gesh shARm',3,13))

#find() - Finds the first occurnace of the character and gives the index, if not available it will return -1
name = "dur's gesh shARma Is a gOod boY?"
print(name.find('Is'))

#index() - Finds the first occurnace of the character and gives the index, if not available it will return syntaxerror
name = "dur's gesh shARma Is a gOod boY?"
print(name.index('esh'))

# """isalnum() - returns True only if the entire string only consists of A-Z,a-z,0-9.If any other characters or punctuations are present, 
# then it returns False."""

name ="dur's gesh shARma Is a gOod boY?"
print(name.isalnum())


# """The isalpha() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or 
# numbers(0-9) are present, then it returns False."""

name ="dursgeshshARmaIsagOodboY"
print(name.isalpha())

#The islower() method returns True if all the characters in the string are lower case, else it returns False.
name ="dursgeshshARmaIsagOodboY"
print(name.islower())

#The isupper() method returns True if all the characters in the string are upper case, else it returns False.
name ="dursgeshshARmaIsagOodboY"
name2 = name.upper()
print(name2.isupper())

#The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
name ="dursgeshshARm, aIsagOodboY\n"
print(name.isprintable())

# The isspace() method returns True only and only if the string contains white spaces, else returns False.
name ="   "
print(name.isspace())
name ="dursgeshshARm, aIsagOodboY\n"
print(name.isprintable())

#The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
#The title() method capitalizes each letter of the word within the string.
name ="Dursgesh shARma Is a gOod boY"
name2 = name.title()
print(name2.istitle())

#The isupper() method returns True if all the characters in the string are upper case, else it returns False.
name ="dursgeshshARm, aIsagOodboY\n"
print(name.isupper())

#The islower() method returns True if all the characters in the string are lower case, else it returns False.
name ="dursgeshshARm, aIsagOodboY\n"
print(name.islower())

#The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
name = "dursgeshshARmaIsagOodboY"
print(name.swapcase())

















