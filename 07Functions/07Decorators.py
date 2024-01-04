import os 
os.system("cls")

# function decorators
print("Function decorators")
# function decorators: function which takes other function as input,
# add aditional functionalities and return it
# callable python objects
# function--->Decorators--->function
# callable pyhton objects which modifies other function/class

# decorator
def decor(printer):
    # func()
    def inner():
        printer()  # existing functionality
        # adding neew functionality
        print("\nwelcome")
        # printer()
    # returns object
    return inner

@decor
def printer():
    # will print welcome message two times
    print("welcome")
    print("welcome")

# printer=decor(printer)  # instead of writing this use @decor above printer function
printer()  # will print welcome message three times

# example 2
print("\nExample 2")

def decor(additon):
    def inner():
        # another local variable result
        result=additon()  # existing functionality
        # new functionality
        num3=float(input("enter third number: "))
        result=result+num3
        return result
    return inner

@decor
def addition():
    num1=float(input("enter first number: "))
    num2=float(input("enter second number: "))
    # local variable result
    result=num1+num2
    return result

# print(addition())
# addition=decor(addition)
print(f"additon is {addition()}")