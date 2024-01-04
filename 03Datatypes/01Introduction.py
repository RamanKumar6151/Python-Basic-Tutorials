# datatypes introduction
import os
os.system("cls")

# Assigning string to a variable
# immutable
print("Assigning string to a variable")
a = 'This is a string'
print (a)
b = "This is a string"
print (b)
c= '''This is a string'''
print (c)

# Declaring a list
# mutable
print("Declaring a list")
L = [1, "a" , "string" , 1+2]
print (L)
#Adding an element in the list
L.append(6)   
print (L)
#Deleting last element from a list
L.pop()
print (L)
#Displaying Second element of the list
print (L[1])

# Tuples
# immutable
# faster than list
tup = (1, "a", "string", 1+2)
print(tup)
print(tup[1])