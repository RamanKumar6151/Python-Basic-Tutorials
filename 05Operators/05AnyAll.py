from os import system
system("cls")

"""
# The any() function in Python is a built-in function that returns True if at least one element of an iterable is True, and False otherwise. It takes an iterable (such as a list, tuple, or any other iterable object) as its argument and evaluates the truthiness of each element in the iterable.

any(iterable)
"""

# lst1=[False for _ in range(5)]
lst1=[False]*5
print(lst1)

lst2=['', 0, "", False, None]

# empty list
lst3=[]

lst4=[False]*4
lst4.append(5)

print(any(lst1))
print(any(lst2))
print(any(lst3))
print(any(lst4))

print("\nall() function")

lst5=[True]*4
print(all(lst5))
lst5.append('')
print(all(lst5))