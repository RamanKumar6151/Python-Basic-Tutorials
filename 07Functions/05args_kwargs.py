import os
os.system("cls")
# *args and **kwargs

print("*arg and **kwarg")
print("1. *arg")
def fun(*arg):
    for i in arg:
        print(i,end=" ")
fun(1,2,3,5,6)

print("\n")
def fun2(arg1,arg2,arg3):
    print(f"{arg1} {arg2} {arg3}")
fun2(*["arg1","arg2","arg3"])

def fun3(arg1,*arg):
    print(f"first argument is {arg1}")
    for  i in arg:
        print(f"the  *arg argumument is {i}",)
fun3("arg1","arg2","arg3")

print("\n**kwargs")
# used to deal with the data structures containing key values pairs of variable length
def fun4(**kwargs):
    for key in kwargs:
        print(f"{key}={kwargs[key]}")
dst={"first":"geeks", "second":"for", "third":"geeks"}
fun4(**dst)
