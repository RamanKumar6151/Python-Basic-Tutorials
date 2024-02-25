# https://www.geeksforgeeks.org/byte-objects-vs-string-python/

from os import system
system("cls")

a='geeksforgeeks'
c=b"geeksforgeeks"
d=c.decode('ASCII')
if(d==a):
    print("decoding succesful")
else:
    print("Decoding unsuccessfull")

"""

In Python, a bytes object is a sequence of bytes. It is an immutable sequence, similar to a string, but instead of representing characters, it represents a sequence of bytes where each byte can have a value from 0 to 255. The bytes type is often used to handle binary data, such as images, sound files, or network protocols.

Here are some ways to create bytes objects:
"""