import os
os.system("cls")

# reversing the list
# using reverse() METHOD--> lst.reverse()
# using reversed() FUNCTION

# A list can be reversed by using the reverse() METHOD in Python.
lst=[1,2,3,"python"]
lst.reverse()  # permanently changes the list
print(lst)

# The reversed() FUNCTION returns a reverse iterator, which can be converted to a list using the list() function.
reversed_list=list(reversed(lst))
print(reversed_list)

# REMOVING THE ELEMENTS
# remove() method
# pop() method

# list.remove(value) method
# Remove method in List will only remove the first occurrence of the searched element.
# ERROR ARISES IF THE ELEMENT DOESN’T EXIST IN THE LIST
lst.remove("python")
print(lst)
# Time Complexity: O(n)
# Space Complexity: O(1)

# list.pop() method
# list.pop(position) method
# remove and return an element from the list, but by default it removes only the last element of the list 
# to remove an element from a specific position of the List, the index of the element is passed as an argument 
print(lst.pop())
lst.pop(0)
print(lst)
# Time Complexity: O(1)/O(n) (O(1) for removing the last element, O(n) for removing the first and middle elements)
# Space Complexity: O(1)

# Append()	Add an element to the end of the list
# Extend()	Add all elements of a list to another list
# Insert()	Insert an item at the defined index
# Remove()	Removes an item from the list
# Clear()	Removes all items from the list

# Index()	Returns the index of the first matched item
print("\nlist.index(element, start, end)")
lst.clear()
lst=[x for x in "Geeks for geeks!" if x!=' ']
print(f"lst={lst}")
print(f"lst.index('e')={lst.index('e')}")
print(f"lst.index('e',2,5)={lst.index('e',2,5)}")
print(f"lst.index('e',7)={lst.index('e',7)}")

# Count()	Returns the count of the number of items passed as an argument
print(f"lst.count('e')={lst.count('e')}")

# Sort()	Sort items in a list in ascending order
# Reverse()	Reverse the order of items in the list
# copy()	Returns a copy of the list
import copy

copy_lst=lst.copy()
print(f"copy_lst={copy_lst}")

deep_copy_lst=lst
lst.reverse()
print(f"deep_copy_lst={deep_copy_lst}")

# pop()	Removes and returns the item at the specified index. If no index is provided, it removes and returns the last item.