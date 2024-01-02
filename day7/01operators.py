# https://www.geeksforgeeks.org/python-operators/

import os
os.system("cls")
#  operators introduction

# arithmetic operator
# precedence in arithmetic operator
# P(paranthesis)>E(exponential)>M(multiplication and division have same precedence)>D(division)>A(addition)>S(subtraction)
# PEMDAS

# comparision operator
# precedence 
# arithmetic operators> comparison operator(all comparison op have same precedence)

# logical operator
# precedence
# not>and>or

# bitwise operator
# precedence
# NOT(~)>SHIFT(>>,<<)>AND(&)>XOR(^)>OR(|)
# performs bit by bit operations
import os
os.system("cls")

print("bitwise and operator")
print(7&4)
if(1&2):
    print("1&2=1")
elif(1 and 2):
    print("1and2=1")
print("bitwise or operator")
print(7|4)

print("left shift")
print(3<<1)
print(3<<4)
# leftOperand<<rightOperand
# output will be (leftOperand)*2^(rightOperand)

print("right shift")
print(3>>1)
# leftOperand<<rightOperand
# output will be (leftOperand)/2^(rightOperand)
print(3>>4)
print(32>>4)

print("bitwise XOR operator")
print(7^3)
print(7^8)

# identity operator
# is (true if operands are same, else false)
# is not(true if operands are not same, else false)
print("identity operator")
a=10
b=20
c=a
d=10
print(f"a is c {a is c}")
print(f"a is b {a is not b}")
print(f"a is d {a is d}")

print("ternary operator")
print(f"a={a}")
print(f"'a if a>b else b' a={a if a>b else b}")

# associativity: left to right
# NO IDEA HOW BITWISE(~) OPERATOR WORKS
