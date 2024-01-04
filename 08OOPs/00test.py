import os
os.system("cls")

# intro
"""
class Person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def inp(self):
        pass

    def display(self):
        print(f"name: {self.name}")
        print(f"idnumber: {self.idnumber}")
    def isEmployee(self):
        return False
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        super().__init__(name, idnumber)
        self.salary=salary
        self.post=post
    def display(self):
        print(f"name: {self.name}")
        print(f"idnumber: {self.idnumber}")
        print(f"post: {self.post}")
        print(f"salary: {self.salary}")
    def isEmployee(self):
        return True
obj_person=Person("ram",678282)
# obj_person=Person(*[x for x in input("enter name an idnumber: ").split()])
obj_person.display()
# print(type(obj_person.idnumber))
print("is employee {}".format(obj_person.isEmployee()))
obj_employee=Employee("ram",23456,45677,"po")
obj_employee.display()
print("is employee {}".format(obj_employee.isEmployee()))
"""
# class and objects

# other names can be used instead of self
"""
class Dog:
    def __init__(someone, name, age):
        someone.name=name
        someone.age=age
    # def fun(self):
    #     print(self.name)
    def __str__(self) -> str:
        return f"name: {self.name} age: {self.age}"
obj_dog=Dog("Divine wolf",30000000)
# print(obj_dog.name, obj_dog.age)
# obj_dog.fun()
print(obj_dog)  #  without __str__( ) > <__main__.Dog object at 0x000002511B7BB310>
"""

# constructor
# def __init__(self):
# default constructor: one parameter, simple, only self
# parametrized constructor: more than one parameter, first paarmeter self, other parmateter provided by programmer
"""
class Addition:
    # class attributes
    first=0
    second=0
    answer=0

    # parametrized constructor
    def __init__(self,f,s):
        self.first=f
        self.second=s
    def calculate(self):
        self.answer=self.first+self.second
        return self.answer
    def __str__(self) -> str:
        return f"{self.first}+{self.second}={self.calculate()}"
obj_add=Addition(12,45)
print(obj_add)
"""
# destructors
# __del__() executezs when object gets detstroyed

class test:
    def __init__(self) -> None:
        print("constructor")
    def __del__(self):
        print("destructor")
obj=test()
del obj