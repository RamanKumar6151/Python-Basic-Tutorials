import os
os.system("cls")
# global and nonlocal keywords
a=10
def read():
    print(a) 
def mod1():
    global a
    a=5
def mod2():
    global a
    a=15
read()
mod1()
read()
mod2()
read()

# non local
print("non loacal keyword")
def outer():
    a=10
    def inner():
        nonlocal a
        a=5
    inner()
    print(a)
outer() 

# namespaces
print("namespaces")
def some_outer_function():
    print("inside some inner function")
    def some_inner_function():
        global var
        var=10
        print("inside inner function value of var",var)
    some_inner_function()
    print("try printing var from outer function",var) #will show an error
some_outer_function()