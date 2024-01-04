import os
os.system("cls")
print(type(b"string with b"))
import keyword
if "and" in keyword.kwlist:
    # condition true
    print("1")
else:
    # condition false
    print("0")
# total 35 keywords 
print(len(keyword.kwlist))