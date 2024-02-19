# multiple user inputs
import os
os.system("cls")

# to take as desired input
# Using split() method
# Using List comprehension

# split()
# Generally, users use a split() method to split a Python string
# input().split(separator, maxsplit)
num1,num2=input("enter two values").split()
print(f"{num1} {num2}")
# print(num1,num2,sep=" ")
print(type(num1))

# taking multiple x,inputs at a time
# and type casting using list() function
# ******************************
x=list(
    map(
        int, input("enter two values: ").split()
        )
    )
print(x)
"""
input("enter x, y: "):

Asks the user to enter values for x and y, separated by a space.
input().split():

Takes the input string and splits it into a list of substrings using whitespace as the separator.
map(int, ...):

Applies the int function to each element of the list, converting the substrings to integers.
list(...):

Creates a list from the mapped values.
x, y = list(...):

Unpacks the values from the list into the variables x and y.
"""
print(type(x))

# ******************************

# list comprehension
# *******************************
x, y= [int(x) for x in input("enter two values").split()]
print(f"{x} {type(x)}")
print(f"{y} {type(y)}")
# *******************************