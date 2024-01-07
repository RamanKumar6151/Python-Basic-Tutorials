from os import system
system("cls")

# dunder methods
print("dunder methods")
# special methods starting and ending with double underscore (__)
# __init__()
# __str__()
# __repr__()

# __init__() to initialize in class

# __str__() to returns human readable string representation or object 
# called by print(), str(), format()
# if not defined then __repr__() is called

# __repr__() returns more information riched string representaion of object
# called by built in repr() funtion

import datetime
mydate1=datetime.datetime.now()
# will print human understandable format
print(f"__str__() string--> mydate1.__str__(): {mydate1.__str__()}")
print(f"str() string--> str(mydate1): {str(mydate1)}")

# will print more information riched format
# can be used to recreate objects
print(f"\n__repr__() string--> mydate1.__repr__(): {mydate1.__repr__()}")
print(f"repr() string--> repr(mydate1): {repr(mydate1)}")

# recreating object using eval(repr(object))
print("\nrecreating object using eval(repr(object))")

# mydate1=datetime.datetime.now()
mydate2=eval(repr(mydate1))  # recreating an object
print(f"repr(mydate1): {repr(mydate1)}")
print(f"repr(mydate2): {repr(mydate2)}")
print(f"mydate1==maydate2: {mydate1==mydate2}")

# __str__() and __repr__() using class
print("\n__str__() and __repr__() using class")
class Ocean:
    def __init__(self, sea_creature_name, sea_creature_age) -> None:
        self.name=sea_creature_name
        self.age=sea_creature_age
    
    # creating __str__() and __repr__()
    def __str__(self) -> str:
        return f"The creature {self.age} years old {self.name}"
    def __repr__(self) -> str:
        return f"Ocean(\'{self.name}\',{self.age})"

# creating an object
c=Ocean("jellyfish",5)
print(f"str(c): {str(c)}")
print(f"repr(c): {repr(c)}")