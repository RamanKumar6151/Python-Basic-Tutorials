import os
os.system("cls")

# help() function
# used to read the documentation
help(print)

# class
class Helper:
    def __init__(self) -> None:
        # helper class in initiialized
        pass
    def  print_help(self):
        # return help descripttion
        print("helper description")

print("\nclass")
help(Helper)
help(Helper.print_help)

print("\nfunctions")
def fun():
    '''docstring, first text after function definition always in triple quotes '''
    return None
print("using __doc__")
print(fun.__doc__)

print("\nusing help()")
help(fun)