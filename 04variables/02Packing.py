# packing and unpacking of variable
import os
os.system("cls")

print("unpacking")
# when we have a list of arguments and function takes those argumnets seperatly

# function takes four arguments and prints them
def fun(a,b,c,d):
    print(a,b,c,d)
    print(f"sum= {a+b+c+d}")
my_list=[1,2,3,4]

# fun(my_list) # will not work
# use * to unpack the list
# number of arguments=lenght of list, else error occurs
fun(*my_list)

# PACKING
# when we dont know number of arguments we use * to pack arguments in function defination
print("packing")
# fun2 performs packing, afyter packing creates a 'tuple args'
def fun2(*args):
    # return sum(args)
    # or
    s=0
    for i in args:
        s=s+i
    return s

print(fun2(1,2,3,4,5))
print(fun2(4,5))

# unpacking and packing
print("packing and unpacking")
def f1(q,w,e):
    print(q,w,e)

def f2(*args):
    # type casting tuple args into list
    print(type(args))  # tuple
    args=list(args)
    args[0]='q'
    args[1]='w'

    # unpacking the args
    # lsit of argguments
    f1(*args)

f2("a","b","c")

# packing and unpacking in dictionary
# use of **
print("packing and unpacking in dictionary **")
print("UNPACKING IN DICTIONARY")
def f2(a,b,c):
    print(a,b,c)
dict={"a":1,"b":2,"c":3}
f2(**dict)

# writting f2(1,**dict) is equivalent to f2(1,b=2,c=3)

# packing in dictionary
print("packing in dictionary")
def f3(**kwargs):
    print(type(kwargs))
    for key in kwargs:
        print(f"{key}={kwargs[key]}")
f3(**dict)
f3(**{"a":1,"b":2,"c":3})