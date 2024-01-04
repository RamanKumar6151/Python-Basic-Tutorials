import os
os.system("cls")
# inheritance

# object: root of all classes
# class class_name(object) same as class class_name: in pyhton 3
# multiple inheritance
print("multiple inheritance")

class Base1():
    def __init__(self) -> None:
        self.str1="Geek1"
        print("Base1")
class Base2(Base1):
    def __init__(self) -> None:
        super().__init__()
        self.str2="Geek2"
        print("Base2")
class Derived(Base2):  # will inherit properties of Base1 through Base2
    def __init__(self) -> None:
        super().__init__()
        print("Derived")
    def printStrs(self):
        print("{} {}".format(self.str1, self.str2))
obj_derived=Derived()
obj_derived.printStrs()

# accessing the parent members in a subclass
# 1. using parent class name
# 2. using super()
print("accessing the parent members in a subclass")
print("1. using parent class name")
class Parent:
    def __init__(self,x) -> None:
        self.x
class Child(Parent):
    def __init__(self,x,y) -> None:
        Parent.x=x
        self.y=y
    def printXY(self):
        print("{} {}".format(Parent.x,self.y))
obj_child=Child(10,20)
obj_child.printXY()

# 2. using super() method
print("using super method")
class Base(object):
    def __init__(self,x) -> None:
        self.x=x
class DerivedBase(Base):
    def __init__(self, x,y) -> None:
        super(DerivedBase, self).__init__(x)
        self.y=y
    def printXY(self):
        print("{} {}".format(Parent.x,self.y))
obj_derivedbase=DerivedBase(10,20)
obj_derivedbase.printXY()