# sets

import os
os.system("cls")

# Set is an unordered collection of data types that is iterable, mutable and has no duplicate elements. The order of elements in a set is undefined though it may consist of various elements. The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set.
# Python program to demonstrate
# Creation of Set in Python
 
# Creating a Set
set1 = set()
print("Initial blank Set: ")
print(set1)
 
# Creating a Set with
# the use of a String
set1 = set("GeeksForGeeks")
print("\nSet with the use of String: ")
print(set1)
 
# Creating a Set with
# the use of Constructor
# (Using object to Store String)
String = 'GeeksForGeeks'
set1 = set(String)
print("\nSet with the use of an Object: " )
print(set1)
 
# Creating a Set with
# the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List: ")
print(set1)
 
# Creating a Set with
# the use of a tuple
t=("Geeks","for","Geeks")
print("\nSet with the use of Tuple: ")
print(set(t))
 
# Creating a Set with
# the use of a dictionary
d={"Geeks":1,"for":2,"Geeks":3}
print("\nSet with the use of Dictionary: ")
print(set(d))

# adding the elements
# set.add() method
# set.update() method

# set.add() method
# Python program to demonstrate
# Addition of elements in a Set
 
# Creating a Set
set1 = set()
print("Initial blank Set: ")
print(set1)
 
# Adding element and tuple to the Set
set1.add(8)
set1.add(9)
set1.add((6, 7))
print("\nSet after Addition of Three elements: ")
print(set1)
 
# Adding elements to the Set
# using Iterator
for i in range(1, 6):
    set1.add(i)
print("\nSet after Addition of elements from 1-5: ")
print(set1)

# Using update() method
# For the addition of two or more elements Update() method is used. The update() method accepts lists, strings, tuples as well as other sets as its arguments. In all of these cases, duplicate elements are avoided.
# Python program to demonstrate
# Addition of elements in a Set
 
# Addition of elements to the Set
# using Update function
set1 = set([4, 5, (6, 7)])
set1.update([10, 11])
print("\nSet after Addition of elements using Update: ")
print(set1)

# Accessing of elements in a set
 
# Creating a set
set1 = set(["Geeks", "For", "Geeks."])
print("\nInitial set")
print(set1)
 
# Accessing element using
# for loop
print("\nElements of set: ")
for i in set1:
    print(i, end=" ")
 
# Checking the element
# using in keyword
print("\n")
print("Geeks" in set1)

# removing the elements from the sets
# using the remove() method
# using the discard() method
# using the pop() method
# using the clear() method

# 1. set.remove(value)
# will give keyerror if value is not in set
# Python program to demonstrate
# Deletion of elements in a Set
 
# Creating a Set
set1 = set([1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12])
print("Initial Set: ")
print(set1)
 
# Removing elements from Set
# using Remove() method
set1.remove(5)
set1.remove(6)
print("\nSet after Removal of two elements: ")
print(set1)
 
# Removing elements from Set
# using Discard() method
set1.discard(8)
set1.discard(9)
print("\nSet after Discarding two elements: ")
print(set1)
 
# Removing elements from Set
# using iterator method
for i in range(1, 5):
    set1.remove(i)
print("\nSet after Removing a range of elements: ")
print(set1)

# Using pop() method:
# Pop() function can also be used to remove and return an element from the set, but it removes only the last element of the set.
# Using clear() method:
# To remove all the elements from the set, clear() method is used. 
#Creating a set
set1 = set([1,2,3,4,5])
print("\n Initial set: ")
print(set1)
 
 
# Removing all the elements from
# Set using clear() method
set1.clear()
print("\nSet after clearing all the elements: ")
print(set1)

# add()	Adds an element to a set
# remove()	Removes an element from a set. If the element is not present in the set, raise a KeyError
# clear()	Removes all elements form a set
# copy()	Returns a shallow copy of a set
# pop()	Removes and returns an arbitrary set element. Raise KeyError if the set is empty
# update()	Updates a set with the union of itself and others
# union()	Returns the union of sets in a new set
# difference()	Returns the difference of two or more sets as a new set
# difference_update()	Removes all elements of another set from this set
# discard()	Removes an element from set if it is a member. (Do nothing if the element is not in set)
# intersection()	Returns the intersection of two sets as a new set
# intersection_update()	Updates the set with the intersection of itself and another
# isdisjoint()	Returns True if two sets have a null intersection
# issubset()	Returns True if another set contains this set
# issuperset()	Returns True if this set contains another set
# symmetric_difference()	Returns the symmetric difference of two sets as a new set
# symmetric_difference_update()	Updates a set with the symmetric difference of itself and another

# frozenset(iterable)
"""
 It is a built-in data type that represents an immutable set. While a regular set (set) is mutable and can be modified after creation, a frozenset is immutable, meaning its elements cannot be changed once it is created.
"""

# creting a frrozenset()
frozen_set=frozenset([1,2,3,4])
print(f"\nfrozen_set= {frozen_set}")
"""
You can perform various set operations on frozenset objects, such as intersection, union, difference, and membership tests, similar to regular sets. However, since frozenset is immutable, you cannot modify it by adding or removing elements.
"""
frozen_set1=frozenset([1,2,3,4])
frozen_set2=frozenset([3,4,5,6])

# set operations
intersection=frozen_set1 & frozen_set2
union=frozen_set1 | frozen_set2
diffrence=frozen_set1 - frozen_set2

print("intersection", intersection)
print("union", union)
print("difference", diffrence)
# Note: While frozenset is supported in Python 3, you should be aware that some set operations and syntax might differ from the mutable set.

# frozen_set.add("he") # will return an error

print("set(enumerate(list('Hackerrank'))) -> ",set(enumerate(list('Hackerrank'))))