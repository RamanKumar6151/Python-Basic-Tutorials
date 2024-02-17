# https://www.geeksforgeeks.org/ordereddict-in-python/
# ordered dict

import os
from collections import OrderedDict

os.system("cls");

# regular dict
print("this is a regular dict")
regular_dict={}
regular_dict['a']=1
regular_dict['b']=2
regular_dict['c']=3
regular_dict['d']=4
for key, values in regular_dict.items():
    print(key,values)\
    
# ordered dict 
print("ordered dict")
od=OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od['d']=4
for key,values in od.items():
    print(key,values)

# if order of key remains unchanged even if its value is changed
print("if order of key remains unchanged even if its value is changed")
od['c']=5
for key,value in od.items():
    print(key,value)

print("OrderedDicts in Python can be compared for equality not only based on their content but also considering the order of insertion.")
# Create two ordered dictionaries with different orderings
od1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od2 = OrderedDict([('c', 3), ('b', 2), ('a', 1)])
 
# Compare the ordered dictionaries for equality
print(od1 == od2) 

print("reverse of a ordered dict")
od1=OrderedDict(reversed(od1.items()))
for key,value in od1.items():
    print(key,value)

print("popitem(last=True)")
print(od1.popitem(last=True))

# Key Insertion at Arbitrary Position in Python Dictionary Ordered
print("Key Insertion at Arbitrary Position in Python Dictionary Ordered")
od3=OrderedDict([('a',1),('b',2),('c',3),('d',4),('e',5)])
print("od3.move_to_end('a')")
od3.move_to_end('a')
for key,value in od3.items():
    print(key,value)
print("od3.move_to_end('b',last=True)")
od3.move_to_end('b',last=True)
for key,value in od3.items():
    print(key,value)