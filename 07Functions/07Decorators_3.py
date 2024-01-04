import os
os.system("cls")

# single decorator for multiple existing functions
print("single decorator for multiple existing functions")

def decor(func):
    def inner(*args):  # variable length arguments
        for num in args[1:]: # args 1 to end
            if num==0:
                return "cannot devide by zero"
        return func(*args)
    return inner

@decor
def div1(a:float, b:float)->float:
    return a/b

@decor
def div2(a:float, b:float, c:float)->float:
    return a/b/c

print(div1(10,5))
print(div1(10,0))

print(div2(0,10,5))
print(div2(0,0,5))