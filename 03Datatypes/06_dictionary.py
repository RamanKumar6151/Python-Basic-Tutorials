import os
os.system("cls")

# Dictionary

# Intro
# collection of keys values
# Values can be of any data type
# Keys can’t be repeated and must be immutable.

# Creating a dictionary
# Adding elemenst is dictionary
# Accessing elements of a Dictionary
# Deleting Elements

# CREATING A DICTIONARY 
# empty dictionary
# using {}
dict1={}
print(f"empty dictionary {dict1}")
# using dict() keyword
dict2=dict()
print(f"empty dictionary 2 using dict() keyword {dict2}")
# creating the dictonary with mixed keys
mixed_dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print(f"Dictionary with the use of Mixed Keys: {mixed_dict}")
# using dict() keyword
mixed_dict = dict({'Name': 'Geeks', 1: [1, 2, 3, 4]})
print(f"Dictionary with the use of Mixed Keys and dict() keyword: {mixed_dict}")
# CREATING A NESTED DICTIONARY
# as shown in the below image
nested_dict = {
    1:"geeks",
    2:"for",
    3:{
        'A':"welcome",
        'B':"to",
        'C':"geeks"
    }
}
  
print(f"nested dictionary {nested_dict}")

if __name__=="__main__":
    pass