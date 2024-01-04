import os
os.system("cls")

# python inheritance
print("Python Inheritance")
# inheritance
# one class derive the properties of another class
# types of inheritance
"""
# 1. single inheritance
#       A
#       |
#       B
# 2. Multilevel inheritance
#       A
#       |
#       B
#       |
#       C
# 3. Heirarchical inhertance
#          A
#         / \
#        B   C
# 4. Multiple inheritance
#      A   B
#       \ /
#        C
"""

# parent class
class Person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber

    def display(self):
        print(f"self.name {self.name}")
        print(f"self.idnumber {self.idnumber}")

    def details(self):
        print(f"my name is self.name {self.name}")
        print(f"my idnumber is self.idnumber {self.idnumber}")

# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary=salary
        self.post=post

        # invoking init of Person
        Person.__init__(self, name, idnumber)
    
    def details(self):
        print(f"My name is self.name {self.name}")
        print(f"My idnumber is self.idnumber {self.idnumber}")
        print(f"My post is self.post {self.post}")

# creation off object or an instance
B=Employee("Raman",6151,75000,"Senior SDE")
B.display()
B.details()

# pyhton polymorphism
print("\nPython polymorphism")
# demonstrates the concept of inherritance and meethod overriding
# subclass can override the methods of parent class

# parent class
class Bird:
    def intro(self):
        print("many types of birds")
    def flight(self):
        print("some fly some don't")

# subclass/child class
class Sparrow(Bird):
    def flight(self):
        print("sparrow flies")

# subclass/child class
class Ostrich(Bird):
    def flight(self):
        print("ostrich dont fly")
        Bird.flight(self)  # self is required here

# driver code
# objects
obj_bird=Bird()
obj_sparrow=Sparrow()
obj_ostrich=Ostrich()

obj_bird.intro()
obj_bird.flight()

print("\n")
obj_sparrow.intro()
obj_sparrow.flight()

print("\n")
obj_ostrich.intro()
obj_ostrich.flight()

print("\nencapsulation")
# puts restriction on accessing variables and methods directly to prevent accidental modification
# __ before variable name is used to create private variables
# private variables: those variables who can only be hanged by the methods of only their own objects
#    __________________
#   (methods | varibles)
#          class


class Super:
    def __init__(self) -> None:
        self.__a=10  # will create a private variable, can't be access beyond given class
        self.c=30
class Sub(Super):
    def __init__(self) -> None:
        Super.__init__(self)
        self.b=20
        # print(self.__a)  # will show error 
        print(f"self.c in Sub class {self.c}")

# __init__() is executed whenever the object is created
obj_sub=Sub()
print(obj_sub.b)
print(obj_sub.c)

# both will show an error
# print(obj.__a)
# print(obj.a)

# will aslo show error
# super_obj=Super()
# print(super_obj.a)

# for data hiding refer to 01Introduction_4.py