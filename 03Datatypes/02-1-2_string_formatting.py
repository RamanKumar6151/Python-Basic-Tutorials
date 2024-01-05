import os
os.system("cls")
# Integers such as Binary, hexadecimal, etc., and floats can be rounded or displayed in the exponent form with the use of format specifiers.
print("binary of 15: {0:b}".format(15))
print("exponential of 15: {0:e}".format(15))
print("float of 15: {0:f}".format(15))
print("hexadecimal of 15: {0:x}".format(15))
print("hexadecimal of 15: {0:X}".format(15))
print("{0:x}".format(16))
#  The given code snippet uses the format method to convert the decimal number 16 into its hexadecimal representation.

# Explanation:

# {0:x}: This is a placeholder within the string for formatting. {0} refers to the first argument in the format method, and :x specifies that the argument should be formatted as a hexadecimal (base-16) number.

# format(16): The format method is called with the argument 16. The number 16 is then converted to its hexadecimal representation.
print("octal of 15: {0:o}".format(15))

# string alignment
print("string alignment")
# left align(<), center align(^), right align(>)
# <10 means that the string should be aligned to the left within a field of width of 10 characters.
str2="{:<10}".format("geeks")
print(str2,"hi")
print(len(str2))
str_temp="{0:b}".format(16)
# aligns and converts to binary at a together
str3="{0:<10b}".format(16)
print(str3,"hii")
print(len(str3))