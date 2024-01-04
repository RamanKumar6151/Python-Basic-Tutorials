import os
os.system("cls")

# global and local variables

# local variable
def f():
    s="i love geeks for geeks";
    print(s)
f()
# using local variable outside the function
# print(s) # error: NameError: name 's' is not defined

# global variable
print("global variables")
s="i love geeks for geeks"
def f2():
    print(s)
f2()

# same name of global and local varible
print("\nsame variable intialized globally and locally")
var="global"
def fun():
    var="local"
    print(var)
print(f"outside the function {var}")
print(f"inside the function",end=" ")
fun()
print("\n")

print("change the value of a global variable inside the function")
def fun2():
    global var2
    var2+=" hola"
    print(f"inside function {var2}")
var2="namaste"
fun2()