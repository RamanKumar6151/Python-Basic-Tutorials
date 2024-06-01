# Linspace--> Linear space
import os
import numpy as np
os.system("cls")
print("Linspace or linear space")
print("generate linearly spaced values")
print("generate the number within the specified numbers that the difference between them will be same")

print("np.linspace(1, 5)\n",np.linspace(1, 5))

# np.lispace(start, end, how many values we want)
print('np.linspace(1,5,10)\n',np.linspace(1,5,10))
print(np.linspace(10,100, 10))

print("\n\nRANDOM")
# np.random.randint
# creating random numbers
# np.random.randint(start, end how many)
print("np.random.randint(start, end how many)")
print("np.random.randint(1,10,10) = ",np.random.randint(1,10,10))
print("np.random.randint(1,10, size=(2,2)) = ")
print(np.random.randint(1,10, size=(2,2)))
print(np.random.randint(100,200, size=(3,5)))

print("\nnp.random.rand(how many)")
# np.random.rand(n) creates n random numbered array between 0 and 1
print("np.random.rand(5)=",np.random.rand(5))
print("np.random.rand(2,3)")
print(np.random.rand(2,3))

print("\nnp.random.randn(how many)")
# np.random.rand(n) creates n random numbered array between 0 and 1
print("np.random.randn(-3,3)=",np.random.randn(3))
print("np.random.randn(2,2)")
print(np.random.randn(2,2))
