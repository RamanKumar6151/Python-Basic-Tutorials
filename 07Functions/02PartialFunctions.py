import os
from functools import  partial
os.system("cls")

# partial functions
def add(a:int,b:int,c:int)->int:
    return 100*a+10*b+c
add2=partial(add,c=1,b=2)
print(add2(10))
print(add2(3))
print(add2(2))
# can be used when the function uses fixed values as arguments but one value is not fixed