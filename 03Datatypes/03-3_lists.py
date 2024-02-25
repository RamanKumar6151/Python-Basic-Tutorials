import os
os.system("cls")
# reduce() function
# apply a particular function passed in its argument to all of the list elements stores the intermediate result and only returns the final summation value
#  This function is defined in “functools” module.
import functools
# At first step, first two elements of sequence are picked and the result is obtained.
# Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
# This process continues till no more elements are left in the container.
# The final returned result is returned and printed on console.

lst=[1,2,3,4]
print("prints the sum of all elements is list\n")
print(f"functools.reduce(lambda a,b: a+b, lst)={functools.reduce(lambda a,b: a+b, lst)}")
print(f"functools.reduce(lambda a,b: a if a>b else b, lst)={functools.reduce(lambda a,b: a if a>b else b, lst)}")
print("reduce() with initializer")
print(f"functools.reduce(lambda a,b: a if a>b else b, lst,10)={functools.reduce(lambda a,b: a if a>b else b, lst,10)}")
# reduce()	apply a particular function passed in its argument to all of the list elements stores the intermediate result and only returns the final summation value

# sum()	Sums up the numbers in the list
"""
Syntax : sum(iterable, start)  

iterable : iterable can be anything list , tuples or dictionaries , but most importantly it should be numbers.
start : this start is added to the sum of  numbers in the iterable. If start is not given in the syntax , it is assumed to be 0.
Possible two more syntaxes

sum(a) :  a is the list , it adds up all the numbers in the list a and takes start to be 0, so returning only the sum of the numbers in the list.
sum(a, start) : this returns the sum of the list + start The sum
"""
print(f"sum(lst): {sum(lst)}")
print(f"sum(lst,3): {sum(lst,3)}")

# max()	return maximum element of a given list
# min()	return minimum element of a given list
# all()	Returns true if all element is true or if the list is empty
# any()	return true if any element of the list is true. if the list is empty, return false
# len()	Returns length of the list or size of the list

# enumerate()	Returns enumerate object of the list
"""
Syntax: enumerate(iterable, start=0)

Parameters:

Iterable: any object that supports iteration
Start: the index value from which the counter is to be started, by default it is 0
Return: Returns an iterator with index and element pairs from the original iterable
"""
# The enumerate() function in Python is a built-in function that is used to add a counter to an iterable and return it as an enumerate object. The syntax of the enumerate() function is as

print("\nSyntax: enumerate(iterable, start=0)")
# creating new list
fruits=["apple", "banana", "mango", "grapes"]
# enumerate_obj=enumerate(fruits, start=1)
enumerate_obj=enumerate(fruits, 1)
fruits_dct=dict(enumerate_obj)
print(fruits_dct)
for ele in enumerate(fruits):
    print(ele)

for count, fruit in enumerate(fruits):
    print(count, fruit)

# accumulate()	apply a particular function passed in its argument to all of the list elements returns a list containing the intermediate results
# filter()	tests if each element of a list is true or not
# map()	returns a list of the results after applying the given function to each item of a given iterable
# lambda()	This function can have any number of arguments but only one expression, which is evaluated and returned.