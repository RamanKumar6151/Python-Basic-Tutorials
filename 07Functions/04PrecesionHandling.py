import os
os.system("cls")
print("precision handling")
# precision handling
# methods to handle precision
# 1. rounding method
# 2. getcontext() method
# 3. math module
# 4. decimal module

# 1. round()
print("\nround() and format()")
print(f"round(8.88888,2) {round(8.88888,2)}")
print("formatted {:.3f}".format(9.999))

# getcontext() decimal module
from decimal import Decimal, getcontext
getcontext().prec=3
result=Decimal('3')/Decimal('9')
print(result)