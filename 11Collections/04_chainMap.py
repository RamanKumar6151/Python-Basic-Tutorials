from os import system
from collections import ChainMap

system('cls')

dict1=dict([('a', 1), ('b', 2), ('c', 3)])
dict2=dict([('d', 4), ('e', 5), ('f', 6)])
chain=ChainMap(dict1,dict2)
print(f"chain.maps: {chain.maps}")
print(f"list(chain.keys)(): {list(chain.keys())}")
print(f"list(chain.values()): {list(chain.values())}")
dict3={'f' : 5 }
print("adding new dictionary in chainmap")
chain.new_child(dict3)
print(chain.maps)

print("value associated with b before reversing")
print(chain['b'])
chain.maps=reversed(chain.maps)

print("value associated with b after reverse")
print(chain['b'])