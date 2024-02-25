from os import system
system("cls")

"""
In Python, there is a convention to indicate that a variable is intended to be private by prefixing its name with an underscore (_). However, it's important to note that this is just a convention, and Python does not enforce the privacy of variables in the way some other languages do.

When a variable is named with a single leading underscore (e.g., _my_variable), it signals to other developers that the variable is intended for internal use within the module or class, and it should not be accessed directly from outside the module or class. It serves as a form of documentation and a hint to other developers about the intended usage.
"""

class MyClass:
    def __init__(self) -> None:
        self._private_variable=42
    def get_private_variable(self):
        return self._private_variable

obj=MyClass()
print(obj.get_private_variable())
print(obj._private_variable)

"""
For stricter control over access, you might consider using name mangling by prefixing the variable name with two underscores (__). This will cause the interpreter to "mangle" the name, making it harder to access from outside the class. However, it's important to note that this is still a form of name hiding rather than true encapsulation.
"""

class newClass():
    def __init__(self) -> None:
        self.__private_variable=43
    def get__private_variable(self):
        return self.__private_variable 

newObj=newClass()
print(newObj.get__private_variable())
# print(newObj.__private_variable)  # will give an AttributeError
print(newObj._newClass__private_variable)   # Accessing the mangled private variable (not recommended)

"""
Again, these are conventions and mechanisms to indicate intent rather than strict access controls. It's generally expected that developers will follow these conventions and use variables responsibly.
"""