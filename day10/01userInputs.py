# 01 python inputs
import os

os.system("cls")
# two inbuilt functions to read the input FROM KEYBOARD
# input()
# raw_input() used in python 2.x
name = input("enter your name: \n")
print(f"your name is : {name}")
# When input() function executes program flow will be stopped until the user has given input.
# input() function takes all the input as a string only

# to take as desired input
num=int(input("enter the num"))
num2=float(input("enter the num: "))

print(f"{name} {num} {num2}")
print("{} {} {}".format(name, num, num2))