import os
import numpy as np
os.system("cls")

a=np.arange(1,11)
print(a)
print(a[1])
print(a[-1])
print(a[1::2])

b=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
print(b)
print(b[0][0])
print(b[2][1])
print(b[0,0])
print(b[2,1])
# printing second column
# : --> refers to row
# b[:,[1]] starts from 0 row and goes all the way too last row, of 1th column
print("b[:,[1]] starts from 0 row and goes all the way too last row, of 1th column")
print(b[:,[1]])
# b[1:,[1]] starts from 1th row and goes all the way too last row, of 1th column
print("b[1:,[1]] starts from 1th row and goes all the way too last row, of 1th column")
print(b[1:,[1]])
# prints elements of column horizontally
print(b[:,1])
print("two columns")
print(b[:,[1,2]])