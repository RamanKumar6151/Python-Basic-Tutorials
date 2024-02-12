# for clear screen
from os import system
system("cls")

# container
# an object which hoolds other object like list, tuples

# importing Counter
from collections import Counter

# Counter
# 1. a subclass of dictionary
# 2. used to count the number of occurences of elements in a container

#  INITIALIZATION
# 1. Sequence of items
# 2. with dictionary containin KEYS AND COUNTS
# 3. with keyword arguments mapping string names counts

print("INITIALIZATION\n")
# 1. Sequence of items
print("1. Sequence of items")
print(f"Counter(['B','B','A','B','C','A','B','B','A','C']): output= {Counter(['B','B','A','B','C','A','B','B','A','C'])}")
print("2. with dictionary containing KEYS AND COUNTS")
print(Counter({'A':3, 'B':5, 'C':2}))

# 2. UPDATATION IN COUNTER
# using uodate method
# creating an empty counter
print("\n2. UPDATATION IN COUNTER")
print("using uodate method")
coun = Counter()
coun.update([1, 2, 3, 1, 2, 1, 1, 2])
print(coun)
coun.update([1, 2, 4])
print(coun)

# 3. SUBTRACT TWO COUNTERS
# using subtract method
print("\n3. SUBTRACT TWO COUNTERS\nusing subtract method")
c1=Counter(A=4, B=3, C=10)
c2=Counter(A=10, B=3, C=4)
c1.subtract(c2)
print(f"c1.subtract(c2): {c1}")

# finding distict count in list
# Create a list
print("\nfinding distict count in list")
lst = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
dict=Counter(lst)
for key in dict:
    if dict[key]==1:
        print(key)
print(dict)

# 4. COUNTER OPERATIONS
# a. accessing the counts
# b. elements frequency
# c. most_common()
# d. arithmetic counter
my_list=[1, 2, 3, 1, 2, 4, 1, 5]
my_counter=Counter(my_list)
print("\n\nCounter OPERATIONS")
print("\na. accessing the counts")
print(f"my_counter= {my_counter}")
print("Accessing a counter")
print(f"my_counter[1]= {my_counter[1]}")
print("\nb. elements frequency")
print(f"my_counter.elements()")
for i in my_counter.elements():
    print(i,end=",")
print("\nc. most_common()")
print(f"my_counter.most_common()={my_counter.most_common()}")
print("\nd. arithmetic counter")
# creating another counter
other_counter=Counter([1,2,2,3])
print(f"other_counter={other_counter}")
print(f"my_counter+other_counter={my_counter+other_counter}")


# 5. USE CASES
# a. counting elements
# b. finding duplicates
print("\n\nUSE CASES")

print("\na. counting elements")
word="apple"
print(f"word={word}")
letter_counts=Counter(word)
print(f"letter_counts={letter_counts}")

print("\nb. finding duplicates")
print(f"letter_counts-Counter(set(word))={letter_counts-Counter(set(word))}")