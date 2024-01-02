# output using print()
import os
os.system("cls")

# Syntax : print(value(s), sep= ‘ ‘, end = ‘\n’, file=file, flush=flush)

# Parameters: 

# value(s): Any value, and as many as you like. Will be converted to a string before printed
# sep=’separator’ : (Optional) Specify how to separate the objects, if there is more than one.Default :’ ‘
# end=’end’: (Optional) Specify what to print at the end.Default : ‘\n’
# file : (Optional) An object with a write method. Default :sys.stdout
# flush : (Optional) A Boolean, specifying if the output is flushed (True) or buffered (False). Default: False
# Return Type: It returns output to the screen

# end parameter
print("hello my name is",end=":")
print("raman Kumar")
print("hello my name is",end=":\n")
print("raman Kumar")

# flush parameter
# The I/Os in Python are generally buffered, meaning they are used in chunks
# flush comes in as it helps users to decide if they need the written content to be buffered or not. By default, it is set to false. 
# If it is set to true, the output will be written as a SEQUENCE OF CHARACTERS one after the other.
import time
count=3
for i in reversed(range(count+1)):
    if i>0:
        print(i,end=">>>")
        time.sleep(1)
    else:
        print("start")
# above code adds text without a trailing newline and then sleeps for one second after each text addition
for i in reversed(range(count+1)):
    if i>0:
        print(i,end=">>>",flush=True)
        time.sleep(1)
    else:
        print("start")

# seperator parameter
date=11
month=9
year=2023
print(date,month,year,sep="-")
# Positional arguments cannot appear after keyword arguments

# file argument
import io
 
# declare a dummy file
dummy_file = io.StringIO()
 
# add message to the dummy file
print('Hello Geeks!!', file=dummy_file)
 
# get the value from dummy file
print(dummy_file.getvalue())

print('Welcome to GeeksforGeeks Python world.!!', file=open('Testfile.txt', 'w'))