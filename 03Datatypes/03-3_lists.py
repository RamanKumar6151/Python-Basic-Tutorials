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

# Let's break down the provided code to understand what it does and then explain the output:

# Explanation of `reduce()`

# 1. **`reduce(function, iterable[, initializer])`**:
#    - `function`: A function of two arguments. This function is applied cumulatively to the items of the iterable.
#    - `iterable`: The sequence of items to be reduced.
#    - `initializer` (optional): If provided, this value is placed before the items of the iterable in the calculation.

# ### Breakdown of the Code

# 1. **`lambda a, b: a if a > b else b`**:
#    - This lambda function takes two arguments, `a` and `b`, and returns the greater of the two.
#    - Essentially, it finds the maximum of the two arguments.

# 2. **`functools.reduce(lambda a, b: a if a > b else b, lst, 10)`**:
#    - `functools.reduce` will apply the lambda function cumulatively to the items in `lst` with an initial value of `10`.

# ### Step-by-Step Execution

# 1. **Initial value**: The `initializer` is `10`, so the first value of `a` is `10`.
# 2. **First iteration**: Compare `10` (initializer) and `1` (first element of `lst`):
#    - `a if a > b else b` becomes `10 if 10 > 1 else 1` => `10`
# 3. **Second iteration**: Compare `10` (result from previous iteration) and `2` (second element of `lst`):
#    - `10 if 10 > 2 else 2` => `10`
# 4. **Third iteration**: Compare `10` and `3`:
#    - `10 if 10 > 3 else 3` => `10`
# 5. **Fourth iteration**: Compare `10` and `4`:
#    - `10 if 10 > 4 else 4` => `10`
# 6. **Fifth iteration**: Compare `10` and `5`:
#    - `10 if 10 > 5 else 5` => `10`

# ### Output

# After all iterations, the result remains `10` because the initializer `10` is greater than all elements in `lst`.

# Therefore, the output of the code will be:

# ```python
# 10
# ```

# This code effectively finds the maximum value between the initializer and all elements in the list. In this case, since `10` is greater than all elements in `lst`, the output is `10`.

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