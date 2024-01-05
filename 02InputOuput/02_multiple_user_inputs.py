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
print(type(x))

# ******************************

# list comprehension
# *******************************
x, y= [int(x) for x in input("enter two values").split()]
print(f"{x} {type(x)}")
print(f"{y} {type(y)}")
# *******************************