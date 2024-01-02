# https://www.geeksforgeeks.org/python-modules/

# We can import the functions, and classes defined in a module to another module using the import statement in some other Python source file.

import os
# using the function of module through dot(.) operator
# moduleName.function()
os.system("cls")  # to clear the screen

# 1. Import Specific Attributes from a Python module
# 2. Import all Names 
# 3. Locating Python Modules
# 4. Renaming the Python Module

# 1. Import Specific Attributes from a Python module
# import math
# or
# importing sqrt() and factorial from the
# module math
from math import sqrt, factorial
# if we simply do "import math", then
# math.sqrt(16) and math.factorial() are required.
print(sqrt(16))
print(factorial(6))

# 2. Import all Names 
# import moduleName *
# importing sqrt() and factorial from the
# module math
# from math import *
 
# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.
# print(sqrt(16))
# print(factorial(6))

# 3. Locating Python Modules
import sys
print(sys.path)
# Here, sys.path is a built-in variable within the sys module. It contains a list of directories that the interpreter will search for the required module.

# 4. Renaming the Python Module
# importing sqrt() and factorial from the
# module math
import math as mt
# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.
print(mt.sqrt(16))
print(mt.factorial(6))