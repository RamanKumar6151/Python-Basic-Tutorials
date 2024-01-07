# lists 2
import os
os.system("cls")

# Getting the size of Python list
print("Getting the size of Python list")
# Creating a List
List1 = []
print(len(List1))
 
# Creating a List of numbers
List2 = [10, 20, 14]
print(len(List2))

# # Python program to take space
# separated input as a string
# split and store it to a list
# and print the string list
 
# input the list as string
string = input("Enter elements (Space-Separated): ")
 
# split the strings and store it to a list
lst = string.split() 
print('The list is:', lst)   # printing the list

# Adding Elements to a Python List
print("Adding Elements to a Python List")
# Python program to demonstrate
# Addition of elements in a List
 
# Creating a List
List = []
print("Initial blank List: ")
print(List)
 
# Addition of Elements in the List
# List.append(value) method
# List.insert(position, value) method
# List.extend() method

print("Addition of Elements in the List")
# list.append(value)
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)
 
# Adding elements to the List
# using Iterator
for i in range(1, 4):
    List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)
 
# Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)
 
# Addition of List to a List
List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)

# list.insert(position,value)
List=[1,2,3,4]
List.insert(3, 12)
List.insert(0, 'Geeks')
print("\nList after performing Insert Operation: ")
print(List)
# Complexities for Adding elements in a Lists(insert() method):
# Time Complexity: O(n)
# Space Complexity: O(1)

# list.extend() method
# can add multiple values at the end
List.extend([8, 'Geeks', 'Always'])
print("\nList after performing Extend Operation: ")
print(List)
# Complexities for Adding elements in a Lists(extend() method):
# Time Complexity: O(n)
# Space Complexity: O(1)

#  lst.extend(1,2,3)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: list.extend() takes exactly one argument (3 given)

# >>> lst.extend([1,2,3])

# >>> lst.append([1,2,3])
# >>> lst
# [1, 2, 3, [1, 2, 3]]