# String data type

# Literak assignment
first = "Mia"
last = "Tresenio"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# consstructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# take a number and take it to a string
# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like taylor swift music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey how are you?

I was just checking in.

                                All good?

'''
print(multiline)


# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\located?'
print(sentence)



# String Methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                               "
multiline = "                                  " + multiline
print(len(multiline)) 

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Matcha".ljust(16, ".") + "$5".rjust(4))

print("")

# string index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# Some methods return boolean data
print(first.startswith("M"))
print(first.endswith("T"))

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data types

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# Float type - had decimals
gpa = 3.28
y = float(1.14)
print(type(gpa))

# Complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)  #real number system
print(comp_value.imag)  # imaginary


# Built-in functions for numbers
print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))

print(round(gpa, 1))

import math

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a  number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data
#zip_value = int("New York")