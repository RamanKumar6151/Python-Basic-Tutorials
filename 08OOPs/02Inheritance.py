import os
os.system("cls")
# inheritance
# one class inherits properties of another class

# class_name(object) is a ancestor class
class Person(object):
    # constructor
    def __init__(self,name):
        self.name=name
    
    # to get name
    def getName(self):
        return self.name
    
    # to check if this person is employee
    def isEmployee(self):
        return False

class Employee(Person):
    def isEmployee(self):
        return True

emp=Person("Geek1")  # an object of Person

print(f"emp.getName() {emp.getName()} emp.isEmployee() {emp.isEmployee()}")
emp=Employee("Geek2")  #an object of Employee
print(f"emp.getName() {emp.getName()} emp.isEmployee() {emp.isEmployee()}")

# subclass() used to check if a class is a subclass()
class Super:
    pass
class Sub(Super):
    pass
print(f"issubclass(Sub, Super) {issubclass(Sub, Super)}")
print(f"issubclass(Super, Sub) {issubclass(Super, Sub)}")
print(f"issubclass(Super, Super) {issubclass(Super, Super)}") 
# will return true ^

obj_super=Super()
obj_sub=Sub()

print("\nisinstance()")
print(f"isinstance(obj_sub, Sub) {isinstance(obj_sub, Sub)}")
print(f"isinstance(obj_super, Super) {isinstance(obj_super, Super)}")
print(f"isinstance(obj_sub, Super) {isinstance(obj_sub, Super)}")
# will return true since it inherits Super ^

print(f"isinstance(obj_super,Sub) {isinstance(obj_super,Sub)}")