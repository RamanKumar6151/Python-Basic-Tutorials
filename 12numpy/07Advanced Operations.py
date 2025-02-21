# https://www.geeksforgeeks.org/numpy-python-set-2-advanced/
# ADVANCE OPERATIONS
import os
import numpy as np
os.system("cls")

# 1. Stacking
# 2. Splitting
# 3. Broadcasting
print("STACKING")
# 1. STACKING: Several arrays can be stacked together along different axes.
    # np.vstack: To stack arrays along vertical axis.
    # np.hstack: To stack arrays along horizontal axis.
    # np.column_stack: To stack 1-D arrays as columns into 2-D arrays.
    # np.concatenate: To stack arrays along specified axis (axis is passed as argument).

a=np.array([[1,2],
            [3,4]])
b=np.array([[5,6],
            [7,8]])
print("vertical stacking\n", np.vstack((a,b)))
print("horizontal stacking\n", np.hstack((a,b)))
c=[5,6]
print("Column stacking\n", np.column_stack((a,c)))
print("concatenate to 1st(vertically, row) axis\n", np.concatenate((a,b), 0))
print("concatenate to 2nd(horizontally, column) axis\n", np.concatenate((a,b), 1))

print("\nSPLITTING")

# 2. SPLITTING:For splitting, we have these functions:
    # np.hsplit: Split array along horizontal axis.
    # np.vsplit: Split array along vertical axis.
    # np.array_split: Split array along specified axis.
a=np.arange(1,13)
a=a.reshape(2,6)
print(a)
print("vertically splitting into 2 parts\n", np.vsplit(a,2))
print("horizontally splitting into 2 parts\n", np.hsplit(a,2))
print("horizontally splitting into 3 parts\n", np.hsplit(a,3))
# print("horizontally splitting into 4 parts\n", np.hsplit(a,4))  # ValueError: array split does not result in an equal division

print("\nBROADCASTING")
# BROADCASTING:The term broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations. Subject to certain constraints, the smaller array is “broadcast” across the larger array so that they have compatible shapes.

a=np.array([1,2,3])
b=2
print("a*b=",a*b)
arr=np.arange(1,10)         
arr=arr.reshape(3,3)
print(arr)
print(arr*2)
a=np.arange(1,10)
b=np.arange(10,19)
print(a/b)
print(a+b)
print(a*b)
print(a-b)
# In above example, the scalar b is stretched to become an array of with the same shape as a so the shapes are compatible for element-by-element multiplication.
# both arrays get stretched.
print("both arrays get stretched.")
a=np.arange(0,31,10)
b=np.array([0,1,2])  # The expression a[:, np.newaxis] changes the shape of a from (4,) to (4, 1), making it a column vector. Broadcasting is then used to add a to b, resulting in a two-dimensional array where each element of a is added to each element of b.
print(a[:,np.newaxis]+b)
# np.newaxis is used in NumPy to increase the dimensions of an existing array by one more dimension, when used once. This is particularly useful for broadcasting operations, where you want to make the shapes of two arrays compatible for element-wise operations.