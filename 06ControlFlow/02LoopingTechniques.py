import os
os.system("cls")

# looping technique
# 1. enumerate()
# 2. zip()
# 3. iteritems()
# 4. items()

# 1. enumerate()
# used loop through containers printing their index no. with their values
print("enumerate()")
print("enumerate with list")
lst=["hi","hello", "namaste"]
for ind,val in enumerate(lst):
    print(f"lst[{ind}]={val}")

print("enumerate with dictionary")
dct={1:"a",2:"b",3:"c",4:"d"}
for key,value in enumerate(dct):
    print(f"dct[{key}]={value}")  # not working as expected

# 2. zip()
# combime two or more containers and print their elements sequentially, runs untill smallest container completes
print("zip()")
for val,key in zip(lst,dct):
    print(f"list[{ind}] dict[{key}]={dct[key]}")

tpl=("a","b","c","d")
for val1,val2 in zip(lst,tpl):
    print(f"list {val1} tuple {val2}")

# can't understand the ouptut
# for val1,val2 in enumerate(zip(lst,tpl)):
#     print(f"list {val1} tuple {val2}")

# zip() also works with same containers

# 3. iteritems() did'nt got any content on gfg, yet

# 4. items()
# same as iteritems(), loops through the dictionary to print key values
# disadvantge compared to iteritems()
# - time consuming
# - may consume more memory

print("dictionary_name.items()")
for key,val in dct.items():
    print(f"{key}={val}")

# test
print("trying enumerate with dictionary: ")
for key,val in enumerate(dct):
    print(f"{key}={val}")
# return sindex of keys and key

# more functions
# 1. sorted
# 2. reversed
print("sorted() and reversed(): ")
lst2=[43,12,34,89,1,3,0,78]
sorted(lst2)
reversed(lst2)
print(lst2)
print(f"sorted(lst2) {sorted(lst2)}")
for i in reversed(lst2):
    print(i,end=" ")
