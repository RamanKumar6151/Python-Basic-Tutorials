import os
os.system("cls")
# map function
# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
# Syntax: map(fun, iter)

# Parameters:

# fun: It is a function to which map passes each element of given iterable.
# iter: It is iterable which is to be mapped.
# NOTE: You can pass one or more iterable to the map() function.

# Returns: Returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)

# NOTE : The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) .  

def addition(n):
    return n+n
numbers=(1,2,3,4)
result=map(addition, numbers)
print(type(result), *result, sep=" ")

# Double all numbers using map and lambda
 
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

# add two lists using map and lambda
lst1=[int(x) for x in range(1,10) if x%2==0]
lst2=[int(x) for x in range(1,10) if x%2!=0]
print("lst1",*lst1, sep=" " )
print("lst2",*lst2, sep=" " )
result=list(map(lambda x,y:x+y,  lst1,lst2))
print("result",*result,sep=" ")
print(result)
l=["mon","tue","wed","thu"]
test=list(map(list,l))
print(test)