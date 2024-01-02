# type conversion
import os
os.system("cls")

# 1. implicit type conversion(automatic), python prevents data loss
# 2. explicit type conversion or type casting , data loss risk

# implict type conversion
print("implicit type conversion")
x=10
y=10.00
print(type(x))
print(type(y))

# explicit type conversion
# 1. int to float
# 2. ord(), hex(), oct()
# 3. tuple(), list(), set() 
# 4. dict(), complex(), str()
# 5. chr()
print("explicit type conversion")

# INT TO FLOAT
# 1. int(a, base)
# 2. float()

# base: base of number inside quotes "10101" base 2
print("int to float")
a='1010'
print(int(a,2))
b="C"
print(int(b,16))
num=78
print(float(num))

# 2. ord() hex() oct()
print("ord() hex() oct()")
print(ord('s'))
# ord() return unicode numbers of a character
print(f"hex(56)={hex(56)}")
print(f"oct(56)={oct(56)}")

# 3. list() tuple() set()
str="geeks"
print(f"list(str)={list(str)}")
print(f"tuple(str)={tuple(str)}")
print(f"set(str)={set(str)}")

# 4. dict() str() complex()
print("dict() str() complex()")
# dict() convert the tuple of order (key, value) into dictionary
tpl=((1,10),(2,20),(3,30))
print(f"dict(tpl) {dict(tpl)}")
# encountering error while using str()
print(f"str(1) {a}")
print(f"complex(1,2) {complex(1,2)}")

# 5. ascii chr()
# number into corresponding ascii character
print(f"chr(76) {chr(76)}")