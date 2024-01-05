import os
os.system("cls")
# Built-In Function

# string.ascii_letters	
# Concatenation of the ascii_lowercase and ascii_uppercase constants.
import string
print(string.ascii_letters)


# string.ascii_lowercase	
# Concatenation of lowercase letters

# string.ascii_uppercase	
# Concatenation of uppercase letters

# string.digits	
# Digit in strings
print(string.digits)

# string.hexdigits	
# Hexadigit in strings
print(string.hexdigits)

# string.letters

# concatenation of the strings lowercase and uppercase

# string.lowercase

# A string must contain lowercase letters.

# string.octdigits

# Octadigit in a string

# string.punctuation

# ASCII characters having punctuation characters.

# string.printable

# String of characters which are printable

# String.endswith()	
# Returns True if a string ends with the given suffix otherwise returns False

# String.startswith()	
# Returns True if a string starts with the given prefix otherwise returns False

# String.isdigit()	
# Returns “True” if all characters in the string are digits, Otherwise, It returns “False”.

# String.isalpha()	
# Returns “True” if all characters in the string are alphabets, Otherwise, It returns “False”.

# string.isdecimal()	
# Returns true if all characters in a string are decimal.

# str.format()	
# one of the string formatting methods in Python3, which allows multiple substitutions and value formatting.

# String.index()	
# Returns the position of the first occurrence of substring in a string

# String.find(substring)	
# Returns the position of the first occurrence of substring in a string else returns "False"

# string.uppercase

# A string must contain uppercase letters.

# string.whitespace()	
# A string containing all characters that are considered whitespace.

# string.swapcase()	
# Method converts all uppercase characters to lowercase and vice versa of the given string, and returns it
# Python program to demonstrate the use of
# swapcase() method 
 
string = "gEEksFORgeeks"
 
# prints after swapping all cases
print(string.swapcase())  
 
string = "geeksforgeeks"
print(string.swapcase()) 
 
string = "GEEKSFORGEEKS"
print(string.swapcase())

# replace()	
# returns a copy of the string where all occurrences of a substring is replaced with another substring.
# string.replace(old, new, count)
# old – old substring you want to replace.
# new – new substring which would replace the old substring.

# count – (Optional ) the number of times you want to replace the old substring with the new substring
string = "Good Morning"
new_string = string.replace("Good", "Great")
  
print(new_string)

# string.Isdecimal	
# Returns true if all characters in a string are decimal

# String.Isalnum	
# Returns true if all the characters in a given string are alphanumeric.

# string.Istitle()	
# Returns True if the string is a title cased string
# When all words in a string begin with uppercase letters and the remaining characters are lowercase letters, the string is called title-cased.  This function ignores digits and special characters.
print("string.Istitle()")
string = "Geeks"
print(string.istitle())
s = 'geeks For Geeks'
print(s.istitle())

# String.title()
# converts the given String into titlecase


# String.partition(seperator)
# splits the string at the first occurrence of the separator and returns a tuple.
print("String.partition(seperator)")
str = "I love Geeks for geeks"
print(str.partition("for"))
# OUTPUT--> ('I love Geeks ', 'for', ' geeks')

# String.Isidentifier	
# Check whether a string is a valid identifier or not.

#  len(string) 	
# Returns the length of the string.

# str.rindex(sub, start, end)
# Returns the highest index of the substring inside the string if substring is found.

# String.Max	
# Returns the highest alphabetical character in a string.

# String.min	
# Returns the minimum alphabetical character in a string.

# String.splitlines	
# Returns a list of lines in the string.

# string.capitalize()	
# Return a word with its first character capitalized.

# string.expandtabs	
# Expand tabs in a string replacing them by one or more spaces

# string.find	
# Return the lowest indexing a sub string. else -1

# string.rfind	
# find the highest index.

# string.count	
# Return the number of (non-overlapping) occurrences of substring sub in string

# string.lower	
# Return a copy of s, but with upper case, letters converted to lower case.

# string.split	
# Return a list of the words of the string, If the optional second argument sep is absent or None

# string.rsplit()	
# Return a list of the words of the string s, scanning s from the end.

# rpartition()	
# Method splits the given string into three parts

# string.splitfields

# Return a list of the words of the string when only used with two arguments.

# string.join	
# Concatenate a list or tuple of words with intervening occurrences of sep.

# string.strip()	
# It returns a copy of the string with both leading and trailing white spaces removed

# string.lstrip	
# Return a copy of the string with leading white spaces removed.

# string.rstrip	
# Return a copy of the string with trailing white spaces removed.

# string.swapcase	
# Converts lower case letters to upper case and vice versa.

# string.translate	
# Translate the characters using table

# string.upper	
# lower case letters converted to upper case.

# string.ljust	
# left-justify in a field of given width.

# string.rjust	
# Right-justify in a field of given width.

# string.center()	
# Center-justify in a field of given width.

# string-zfill	
# Pad a numeric string on the left with zero digits until the given width is reached.

# string.replace	
# Return a copy of string s with all occurrences of substring old replaced by new.

# string.casefold()	
# Returns the string in lowercase which can be used for caseless comparisons.

# string.encode	
# Encodes the string into any encoding supported by Python. The default encoding is utf-8.

# string.maketrans	
# Returns a translation table usable for str.translate()