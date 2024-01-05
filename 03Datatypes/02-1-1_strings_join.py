# Python String join() Method
import os
os.system("cls")

# Python join() is an inbuilt string function in Python used to join elements of the sequence separated by a string separator. This function joins elements of a sequence and makes it a string.
str="-".join("hello")
print(str)

# seperator.join(iterable) 
# Iterable – objects capable of returning their members one at a time. Some examples are List, Tuple, String, Dictionary, and Set
# Return Value: The join() method returns a string concatenated with the elements of iterable. 

# Type Error: If the iterable contains any non-string values, it raises a TypeError exception. 

# joining with empty seperators
list1=["g","e","e","k"]
print("".join(list1))
print("-".join("list1"))

# joining the dictionary
dic={"geek":1,"for":2,"geeks":3}
print("_".join(dic))  # only joins the key values

# custom sepeartor
words=["apple","","banana","","mango"]
seperator="@"
result=seperator.join(word for word in words if word)
print(result)
print(f"bool(\"\")={bool('')}")  # will return False
print(f"bool(\"y\")={bool('y')}")  # will return True

# ********************************
s= 'abc'
print(s.join("xyz"))
print(s.join("wxyz"))
print(s.join("qwxyz"))
# The join method in the code takes a string as argument and returns a new string in which the elements of the original string are concatenated with the separator string that was passed as argument to the join method.

# In the code, the join method is called on the string s and the separator string "xyz" is passed as argument. So, the elements of the original string s are concatenated with the separator string "xyz" to form a new string.

# As the original string s has only one character in each of its three elements, the final string formed is "x" + "a" + "b" + "c" + "y" + "a" + "b" + "c" + "z" = "xabcyabcz".

# So, the output of the program is "xabcyabcz".

# Hope it will help you.