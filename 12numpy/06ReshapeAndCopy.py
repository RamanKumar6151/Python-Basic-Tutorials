# RESHAPE AND COPY
import os
import numpy as np
os.system("cls")

# reshaping 1d array of size 4 into 2d matrix od 2x2
b=np.array([1,2,3,4])
b=b.reshape(2,2)
print(b)
# returns a copy of matrix/array
c=b.copy()
c=np.array([1,2,3,4])
print(c)
print(np.where(c==3))