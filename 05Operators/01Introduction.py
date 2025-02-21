import os
os.system("cls")
#  operators introduction

# arithmetic operator
# precedence in arithmetic operator
# P(paranthesis)>E(exponential)>M(multiplication and division have same precedence)>D(division)>A(addition)>S(subtraction)
# PEMDAS

# comparision operator
# precedence 
# arithmetic operator> comparison operator(all comparison op have same precedence)

# logical operator
# precedence
# not>and>or

# bitwise operator
# precedence
# NOT(~)>SHIFT(>>,<<)>AND(&)>XOR(^)>OR(|)
# performs bit by bit operations

# identity operator
# is (true if operands are same, else false)
# is not(true if operands are not same, else false)
print("identity operator")
a=10
b=20
c=a
d=10
print(f"a is c {a is c}")
print(f"a is not b {a is not b}")
print(f"a is d {a is d}")

print("ternary operator")
print(f"a={a}")
print(f"'a if a>b else b' a={a if a>b else b}")

# associativity: left to right
# NO IDEA HOW BITWISE(~) OPERATOR WORKS
