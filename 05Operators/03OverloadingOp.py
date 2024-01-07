# overloading operators
import os
os.system("cls")

# same operator used for different operations
print(f"addition 10+20= {10+20}")
print(f"concatenation hell+o= {'hell'+'o'}")

# operator overloading: defining the methods for an operator to perform other operations

class A:
    def __init__(self,a):
        self.a=a
    def __add__(self, o):
        return self.a+o.a
ob1=A(1)
ob2=A(2)
print()

# skipping till i understand classes and oops