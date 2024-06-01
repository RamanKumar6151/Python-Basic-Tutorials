# NUMPY INTRODUCTION
# https://www.geeksforgeeks.org/introduction-to-np/
# numpy is a general-purpose array-processing package. It provides a high-performance multidimensional array object and tools for working with these arrays. It is the fundamental package for scientific computing with Python. It is open-source software.
import os
import numpy as np
os.system("cls")

# creating an empty array
print("empty array")
a=np.array([])
print(a)
print(type(a))
print(a.dtype)
print()

a1=np.array([1,2,3])
print(a1)
print()

print("float memebers")
a2=np.array([1.2, 1.3, 11.3])
print(a2)
print()

print("array from tuple")
tpl=(1,2,3,4)
a3=np.array(tpl)
print(a3)
print()

print("a3.ndim ",a3.ndim)
print("a3.size ",a3.size)
print("a3.dtype ", a3.dtype)

print()
# creating 2d array--> matrix
arr=np.array([[1,2], 
              [3, 4]])

# printing the array object
print("Array is of type: ", type(arr))

# printing array dimension
print("No. of dimensions: ", arr.ndim)

# printing the shape of array
print("Shape of array: ", arr.shape)
print(type(arr.shape))

# printing the size(total number of elements) of array
print("sie of array: ", arr.size)

# printing type of elements stored in array
print("Array stores elements of type: ", arr.dtype)

print()
print("3d arrays")
# var=np.array([ [ [],[] ]])
b=np.array([[[1,2],
             [3,4],
             [5,6]]])
print(b)
print("b.shape ", b.shape)
print()

# creates an array from 0 to n-1 or start to end
# np.arange(n)
# np.arange(start, end)  -->start to end-1
# np.arange(start, end, step)
print("np.arange(11)", np.arange(11))
print(np.arange(21))
print(np.arange(1,6))
print(np.arange(10, 21))
print(np.arange(1,10,2))  # --> will give an array of odd numbers 