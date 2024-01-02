# split() method 
import os
os.system("cls")

#  split a string into a list of strings after breaking the given string by the specified separator.
# Syntax : str.split(separator, maxsplit)

# Parameters :
# separator: This is a delimiter. The string splits at this specified separator. If is not provided then any WHITE SPACE is a separator.
# maxsplit: It is a number, which tells us to split the string into maximum of provided number of times. If it is not provided then the default is -1 that means there is no limit.
# Returns : Returns a list of strings after breaking the given string by the specified separator.

# example 1
string="one,two,three"
words=string.split(',')
print(words)

# Time Complexity: O(n)
# Auxiliary Space: O(n)


text = 'geeks for geeks'
  
# Splits at space
print(text.split())
  
word = 'geeks, for, geeks'
  
# Splits at ','
print(word.split(','))
  
word = 'geeks:for:geeks'
  
# Splitting at ':'
print(word.split(':'))
  
# **********************************  
word="catgotabatthensatonamat"
print(word.split("t"))  # prints an extra empty string in a list since the last character is also a 't'

word="catbatmatsat"
print(word.split("t"))#prints an empty string in a list since the last character is also a 't'
# but
print("caTmaTsaToR".split("T"))

# when maxsplit is given
print("caTmaTsaToR".split("T",1))
print("caTmaTsaToR".split("T",2))
print("caTmaTsaToR".split("T",3))