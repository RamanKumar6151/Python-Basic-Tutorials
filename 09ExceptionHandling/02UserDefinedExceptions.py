from os import system
system("cls")

# user defined exceptions
print("user defined exceptions")

class MyError(Exception):  #inheritng exception class
    def __init__(self,value) -> None:
        self.value=value
    def __str__(self) -> str:
        return(repr(self.value))

try:
    raise(MyError(3*2))
except MyError as error:
    print(f"a new exception occured: ", error.value)

# too complex to understand