from os import system
system("cls")

# exception handling


# 1. SyntaxError
# 2. TypeError
# 3. NameError
# 4. IndexError
# 5. KeyError
# 6. ValueError
# 7. AttributeError
# 8. IOError
# 9. ZeroDivisionError
# 10. ImportError

# Exception: are raised when program is syntatctically correct
# but the code tesults in an errror which changes the flow of control

a=[1,2,3]
try:
    print(f"a[1]={a[1]}")
    
    print(f"a[3]={a[3]}")  # will raise IndexError
except:
    print("error occured")

# catching the specific exception
print("catching the speecific exception")
def fun(a):
    if a<4:
        b=a/(a-3)
    print(f"value of b={b}")
try:
    fun(5)
    fun(3)
except ZeroDivisionError:
    print("ZeroDivisionError occured")
except NameError:
    print("NameError")

# try except else clause
print("try except else clause")
def AbyB(a,b):
    try: 
        c=((a+b)/(a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(f"c={c}")
AbyB(2,3)
AbyB(3,3)

# finally keyword
print("\nfinally keyword")

# try:
#   some code
# except :
#   optional block
#   handles the exception
# else:
#   executes if  no error occurs
# finally:
#   some code(always executed)

try:
    5//0
except ZeroDivisionError:
    print("zero division error")
finally:
    print("finally always exeecuted")

# raise
print("raising exception")
# using raise keeyword
try:
    raise NameError("hi there")
except NameError:
    print("an exception")
    raise

# for raise keyword refer to 01ExceptionHandling.py