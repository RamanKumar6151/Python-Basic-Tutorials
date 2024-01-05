# output formatting
# using sytring ,modulo operator(%)
import os
os.system("cls")

# <format_string> % <values>
print("%d %s cost $%.2f"%(6, "banana", 1.74))

welcome_scentence="hello my name is %s"%"graham"
print(welcome_scentence)

# %[<flags>][<width>].[<precision>]<type>
# The % character and the <type> component are required. The remaining components, shown in square brackets, are optional
# d, i, u	Decimal integer
# x, X	    Hexadecimal integer
# o	        Octal integer
# f, F	    Floating-point
# e, E	    E notation
# g, G	    Floating-point or E notation
# c	        Single character
# s, r, a	String
# %	Single '%' character

# integer conversion type
print("integer conversion type")
# The d, i, u, x, X, and o conversion types correspond to integer values.
# d, i, and u are functionally equivalent.
print("%d %i %u"%(1,2,3))

# hexadecimal and octal conversion
print("hexadecimal and octal conversion")
print("hexadecimal of 10: %x, %X"%(10, 10))
# Using lowercase x produces lowercase output, and using uppercase X produces uppercase output
print("octal of 10: %o"%10)
# Note: Uppercase O isn’t a valid conversion type.

# floating point conversion
print("floating point conversion")
print("%d"%(3.45))#will print integer 3
print("%f %F"%(3.12159, 3.14))
print("%e %E"%(1000.0, 1000.0))
print("g and G notaions")
print("%g"%3.14)
print("%G"%3.14)
print("%g"%0.00000003)
print("%G"%0.00000003)

# character conversion types
print("character conversion types")
# c conversion type inserts a single character
print("%c"%"y")
print("%c"%97)
#  s, r, and a produce string output using the built-in functions str(), repr(), and ascii(), respectively
print("%s" % "Café ☕️")
print("%r" % "Café ☕️")
#  %a, Python converts the Unicode characters to their ASCII representation.
print("%a" % "Café ☕️")

# The Literal Percent Character (%%)
print("The Literal Percent Character (%%)")
print("Get %d%% off on %s today only!" % (30, "bananas"))
# If the output is shorter than <width>, then by default, it’s right-justified in a field that is <width> characters wide and padded with ASCII space characters on the left
print("%5s"%"foo")#two spaces added before string
print("%5s"%"4")#four spaces added before th string
# if length is greater than width then nothing happens
print("%2d" % 1234)