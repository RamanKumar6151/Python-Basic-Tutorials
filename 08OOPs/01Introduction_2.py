import os
os.system("cls")

print("__init__() method")
# __init__() method
# a constructor
# used to initialize the values or assign values

# creating the class
class Person:

    # intit method or constructor
    def __init__(self,name) -> None:
        self.name=name

    # self represents instance of class and binds the arguments with the given arguments

    # sample method
    def say_hi(self):
        print(f"hello my name is {self.name}")

# objects
P1=Person("Raman")
P1.say_hi()
P2=Person("Hrittik")
P2.say_hi()
P3=Person("Raj")
P3.say_hi()

print("\n__init__() method with inheritence")
# inheritance: one claass inherits properties form other class

class A(object):
    def __init__(self,something):
        print("A init called ")
        self.something=something

class B(A):
    def __init__(self, something):
        # calling init of parent class
        A.__init__(self,something)
        print("B init called")
        self.something=something
        A.__init__(self,something)

obj=B("something")

# the init method of a class will be called in the order of init methods call

# i was unable to understand anything beyond it

# may return to 01Introduction.py