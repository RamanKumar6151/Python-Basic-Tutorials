import os
import numpy as np
os.system("cls")

# an array of three 1's, float values
print("an array of three 1's, float values")
print(np.ones(3), "\n")

# an array of five 1's , all int value
print("an array of five 1's , all int value")
print(np.ones(5, dtype="int"), "\n")

# a 2d array containing 1's
print("a 2d array containing 1's")
print(np.ones((2,2)), "\n")

# a 2d array containing 1's, all int values
print("a 2d array containing 1's, all int")
print(np.ones((2,2), dtype="int"), "\n")

# an array with all zeroes
print("an array with all zeroes")
print(np.zeros(5, dtype="int"))
print(np.zeros((2,3)))

print("\n\nIDENTITY MATRIX")
print(np.identity(2))
print(np.identity(2, dtype="int"))
# print(np.identity(2, 3))  # will give error, use np.eye(r,c)
print(np.eye(2,3))
# print(np.eye((2,3), dtype='int'))  # will give an error

print("\n\nFULL")
print(np.full((2,3), 10))