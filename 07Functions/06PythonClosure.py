import os
os.system("cls")

# closure: a technique by wwhich the data gets attatched to the code

# closures are function objects that rememenbers values in the enclosing scope even if tey are not present in the memory 

# function closure
print("function closure")

print("\nfunction as object")
# function
def o():
    print("hello")
# object
print(o)
print(type(o))

print("\nnested function")
def outer():
    x=100
    print("hello")
    # nested function
    def inner():
        y=200
        print("bye")
    inner()

# inner()  # NameError
outer()

# aliasing the function
print("\naliasing the function")
# function name represent the object
new=outer
new()

# closures in function
print("\nclosure in function")
def outer():
    def inner():
        x=200
        return x
    # returns x=200
    # return inner()

    # returns th object of inner()
    return inner
    # use new=outer(), then print it

# print(outer())
# aliasing the function
# new=outer()
# print(new())

# aliasing same as the local scope inner
print("aliasing same as the local scope inner")
print("inner=outer()")
inner=outer()
# this inner variable has global scope
# after aliasing the grabage collector clears the memory of outer(), but since the value is enclosed in outer it is accessed by the global inner
print(f"inner() will give {inner()}")