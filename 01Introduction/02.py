# python keywords

import os
os.system("cls")

# The b literal in front of the string literal means that the given string is in bytes' format. The b literal converts string into byte format. In this format bytes are actual data and string is an abstraction. A byte is a collection of 8 bits.

# for more information check following links
# https://www.tutorialspoint.com/What-does-the-b-character-do-in-front-of-a-string-literal-in-Python#:~:text=The%20b%20literal%20in%20front,a%20collection%20of%208%20bits.
# https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal
print(type(b"string with b"))

import keyword
if "and" in keyword.kwlist:
    # condition true
    print("1")
else:
    # condition false
    print("0")
# total 35 keywords 
print(len(keyword.kwlist))

flag=keyword.iskeyword("for")
print(flag)