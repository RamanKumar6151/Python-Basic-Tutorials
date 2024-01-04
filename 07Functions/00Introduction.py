import os
os.system("cls")
# functions introduction
# a block of statements that return a specific task
# def function_name(parameters):
#   statement
#   return expression

# creating a function
def fun():
    print("welcome to gfg")

# calling a function
fun()

# defining a function using parameters
# def function_name(parameter: data_type)-> return type:
#   "docstring"
#   body of function
#   return expression
def add(num1: int, num2: int)-> int:
    # add two numbers
    num3=num1+num2
    return num3

# calling the function
print(f"add(4,5) {add(4,5)}")

# function to check if number is prime
def is_prime(num: int)-> bool:
    if num in [2,3]:
        return True
    if(num==1)or(num%2==0):
        return False
    r=3
    while(r*r<num):
        if(num%r==0):
            return False
        r+=2
        return True
print(f"is_prime(78) {is_prime(78)} is_prime(79) {is_prime(79)}")

# function arguments
# values passed inside paranthesis ofthe function
# function to check even odd
def evenOdd(num: int)-> str:
    if(num%2==0):
        # print("even")
        return "even"
    else:
        # print("odd")
        return "odd"
print(f"evenOdd(10) {evenOdd(10)} evenOdd(11) {evenOdd(11)}")

# types of arguments
# 1. default arguments
# 2. keyword/named arguments
# 3. positional arguments
# 4. arbitrary arguments
print("Arguments")
# 1. DEFAULT ARGUMENTS
# parameter which assumes default value if value is not given
print("11. default arguments")
def myFun(x: int, y=20):
    print(f"x {x}")
    print(f"y {y}")
myFun(10)

# keyword/named arguments
# allows to write values for arguments without knowing their position
print("2. keyword?named arguments")
def name(firstname: str, lastname: str)-> str:
    fullname=firstname+" "+lastname
    return fullname

print(f"name(lastname='kumar', firstname='raman') {name(lastname='kumar', firstname='raman')}")

# can't understand positional arguments except for values need to be given in order of arguments

# 2. arbitrary kyword, *arg, **kwarg
print("4. arbitrary keyword")
def fun2(*arg):
    for i in arg:
        print(i)
fun2(1,2,3,4,5,6)
# check 04variables/02Packing.py for more

# function inside a function or nested functions
print("\nnested functions")
def outer():
    s="gfg"
    def inner():
        print(s)
    inner()

outer()

# anonymous functions
# created using lambda keyword
print("anonymous functions using lambda")
def cube(x: int)->int:
    return x**3
# using lambda
cube2=lambda x: x**3
print(f"lambda x: x**3 where x=2 {cube2(2)}")