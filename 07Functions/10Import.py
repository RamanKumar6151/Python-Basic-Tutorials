import os
os.system("cls")
#  __import__()
# importing the module during runtime

print("__import__()")
# help(__import__)

# importing numpy
# np=__import__('numpy',globals(),locals(),[],0)
# a=np.array([1,2,3])
# print(type(a))

# importing array() and complex() from numpy
np=__import__("numpy",globals(),locals(),["array","complex"],0)
print(np.complex128(3))
print(np.array([1,2,3]))