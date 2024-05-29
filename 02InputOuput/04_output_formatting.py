# Output formatting
import os
os.system("cls")

# ways to format output using String Method in Python. 

# 1. Using String Modulo Operator(%)
# 2. Using Format Method
# 3. Using The String Method
# 4. Python’s Format Conversion Rule

# string modulao operator
print("geeks:%2d, portal:%5.2f"%(1,05.333))
print("geeks:%2d, portal:%05.2f"%(1,05.333))
print("geeks:%2d, portal:%5.4f"%(1,05.333))

print("Total students : %3d, Boys : %2d" % (240, 120))   # print integer value
print("%4.2f"%(123.333))

# %[flags][width][.precision]type 
# The first placeholder ‘%2d’ is used for the first component of our tuple, i.e. the integer 1. It will be printed with 2 characters, and as 1 consists of only one digit, the output is padded with 1 leading blank.

# The second placeholder ‘%5.2f’ is for a float number. Like other placeholders, it’s introduced with the % character. It specifies the total number of digits the string should contain, including the decimal point and all the digits, both before and after the decimal point. 

# Our float number 05.333 is formatted with 5 characters and a precision of 2, denoted by the number following the ‘.’ in the placeholder. The last character ‘f’ indicates that the placeholder represents a float value.

# %05.2f: This specifies a floating-point number (f) that should be formatted with a width of at least 5 characters, including the decimal point and 2 digits after the decimal point. If the number is shorter than 5 characters, it will be padded with zeros (0) on the left. 

# format method
print('I love {} for "{}!"'.format('Geeks', 'Geeks'))
 
# using format() method and referring a position of the object
print('{0} and {1}'.format('Geeks', 'Portal'))
 
print('{1} and {0}'.format('Geeks', 'Portal'))
print('{1} and {0}'.format('Geeks', 'Portal'))
 
print(f"I love {'Geeks'} for \"{'Geeks'}!\"")
 
# using format() method and referring a position of the object
print(f"{'Geeks'} and {'Portal'}")

# The brackets and characters within them (called format fields) are replaced with the objects passed into the format() method

# using string methods?????