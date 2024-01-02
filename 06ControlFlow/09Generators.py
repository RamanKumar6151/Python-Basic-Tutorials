import os
os.system("cls")

# Generators
# function that returns an iterator using yield keyword
# use of yield keyword instead of return
# def generator_name():
#   yield statement

# a simple genartor
def gen1():
    yield 1
    yield 2
    yield 3

# iterating over generator using loop
# for i in gen1():
#     print(i)
temp=gen1()
while(True):
    try:
        # print(next(gen1()))  # will give an infinite loop
        print(next(temp))
    except:
        break