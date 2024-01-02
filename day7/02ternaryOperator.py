# https://www.geeksforgeeks.org/ternary-operator-in-python/

import os
os.system("cls")

# ternary operator
a,b,c=10,20,30

print("ternary operator")
print(f"a={a}")
print(f"'a if a>b else b' a={a if a>b else b}")

print("a is greater" if a>b else "b is greater" if b>c else "c is greater")

# using tuples
print("using tuples")
print(("value at index 0 printed because 0 returned","value at index 1 printed because 1 returned") [b>a])

# using dictionaries
print({True:"a={} is printed because true is returned".format(10), False:"b={} is printed because false is returned".format(20)}[a<b])
print({True:"a={} is printed because true is returned".format(10), False:"b={} is printed because false is returned".format(20)}[a<b])