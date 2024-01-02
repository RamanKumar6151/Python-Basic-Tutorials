import os
os.system("cls")

# multiple decorator
print("Multiple Decorators on a single function")

def decor1(func):
    def inner():
        # func()  # raman kumar
        return func().title()
    return inner

def decor2(func):
    def inner():
        # func()  # Raman Kumar
        return func().split(" ")
    return inner

@decor2  # will execute second
@decor1  # wiil execute first
def get_name():
    name=input("Enter first number: ")  # raman
    sirname=input("Enter sirname: ")  # kumar
    full_name=name+" "+sirname
    return full_name

# print(get_name())
# get_name=decor1(get_name)
# get_name=decor2(get_name)
print(get_name())