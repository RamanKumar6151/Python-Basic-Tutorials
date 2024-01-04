import os
os.system("cls")

# ADDING ELEMENTS IN DICTIONARY
# Dict[Key] = ‘Value’
# Updating an existing value update() keyword

dict1={0:"a", 1:"b", 2:"c"}
dict1[4]="d"
print(f"after adding the element: {dict1}")

# CHANGING THE ELEMENTS 
dict1[4]="changed"
print(f"after changing the value: {dict1}")

# ACCESSING ELEMENTS OF A DICTIONARY
# using key
# using get() method
# USING KEY
print(f"accessing the element using key dict1[0]: {dict1[0]}")
# USING GET() METHOD dict1.get(key)
print(f"accessing the elemenst using the get() method dict1.get(4): {dict1.get(4)}")
# IN NESTED DICTIONARY
Dict = {'Dict1': {1: 'Geeks'},
        'Dict2': {'Name': 'For'}}
  
# Accessing element using key
print("nested dictionaries")
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])

# DELETING THE ELEMENTS
# using del() function
del(dict1[4])
print(f"after deleting dict1[4] {dict1}")

# dic.clear()	Remove all the elements from the dictionary
# dict.copy()	Returns a copy of the dictionary
# dict.get(key, default = “None”)	 Returns the value of specified key
# dict.items()	 Returns a list containing a tuple for each key value pair
# dict.keys()	 Returns a list containing dictionary’s keys
# dict.update(dict2)	Updates dictionary with specified key-value pairs
# dict.values()	 Returns a list of all the values of dictionary
# pop()	 Remove the element with specified key
# popItem()	Removes the last inserted key-value pair
#  dict.setdefault(key,default= “None”)	set the key to the default value if the key is not specified in the dictionary
# dict.has_key(key)	returns true if the dictionary contains the specified key.

# demo for all dictionary methods
dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}

# copy() method
dict2 = dict1.copy()
print(dict2)

# clear() method
dict1.clear()
print(dict1)

# get() method
print(dict2.get(1))

# items() method
print(dict2.items())

# keys() method
print(dict2.keys())

# pop() method
dict2.pop(4)
print(dict2)

# popitem() method
dict2.popitem()
print(dict2)

# update() method
dict2.update({3: "Scala"})
print(dict2)

# values() method
print(dict2.values())
