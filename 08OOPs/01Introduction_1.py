import os
os.system("cls")

# class and objects
# created using class keyword
# attribute: variable used in class
# can be used by class_object.attribute_name

# class dog:
#     pass

# object
# refers to real world entity having
# state: refers to attribute of an object
# behaviour: refers to methods of an object
# identity: refers to unique name of object

# creating an object
# obj=dog()

# methods must have 'self' attribute

# __init__() method
# refer to 01Introduction_2.py
# arrived from 01Introduction_2.py.
# init method run as soon as the class in initialized

class Dog:
    # class attributes
    attr1="mama1"
    # instance attribute
    def __init__(self,name):
        self.name=name

# driver code
# object instantiation
Rodger=Dog("Rodger")
Tommy=Dog("Tommy")

# accesing the class attributes
# objectName.__class__.atrributeName
print(f"\naccesing the class attributes")
# ********************************************
print(f"Rodger is a 'Rodger.__class__.attr1' {Rodger.__class__.attr1}")
print(f"Tommy is a 'Tommy.__class__.attr1' {Tommy.__class__.attr1}")
# ********************************************

# accessing the instance attribute
print("\naccessing the instance attribute")
print(f"My name is 'Rodger.name' {Rodger.name}")
print(f"My name is 'Tommy.name' {Tommy.name}")

# python inheritance 
# refer to 01Introduction_3.py