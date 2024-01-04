import os
os.system("cls")
#Program to reverse a string
print("Program to reverse a string")
gfg = "geeksforgeeks"
print(gfg[::-1])
# reversing the string using join()
print("".join(reversed(gfg)))
print(reversed(gfg))#doees not works

# DELETING/UPDATING FROM A STRING
# In Python, the Updation or deletion of characters from a String is not allowed
# using sstring slicing and concatenation we can store the string in a different variable without unwanted parts
print("DELETING/UPDATING FROM A STRING")
str1="hi"
print(str1)
# deleting entire string
del str1
# print(str1) will show error
print("to manipulate string")
str1="hello, I'm am geek"
# removing a character from string
str2=str1[:2] +str1[3:]
print(str2)

# ignore the escape sequences in a String, r or R is used
print(r"hello \nhi")

print("Formatting the string")
# # Python Program for
# Formatting of Strings
 
# Default order
String1 = "{} {} {}".format('Geeks', 'For', 'Life')
print("Print String in default order: ")
print(String1)
 
# Positional Formatting
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life')
print("\nPrint String in Positional order: ")
print(String1)
 
# Keyword Formatting
String1 = "{l} {f} {g}".format(g='Geeks', f='For', l='Life')
print("\nPrint String in order of Keywords: ")
print(String1)

# print("{1} {f} {g}".format(g='Geeks', f='For', l='Life')) #will show index error