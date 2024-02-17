from os import system
from collections import defaultdict

system("cls")

# creating a default function
# def def_value():
#     print("Not Present")
# defDict=defaultdict(def_value)
defDict=defaultdict(lambda: "not present")
defDict['a']=1
defDict['b']=2
defDict['c']=3
print(defDict.__missing__('a'))
print(defDict.__missing__('d'))