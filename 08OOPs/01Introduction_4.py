import os
os.system("cls")

#  data hiding: hidng informations
# __ before v attributes name allow them not to be directly visible outside

class Myclass:    
    # hidden variable
    __hiddenVariable=0
    def add(self, increment):
        # accessing the hidden variable
        self.__hiddenVariable+=increment
        print(self.__hiddenVariable)

obj_myclass=Myclass()
obj_myclass.add(3)
obj_myclass.add(5)

# print(f"\nobj_myclass.__hiddenVariable {obj_myclass.__hiddenVariable}")  # will give an error
# hidden variables can't be accessed directly
# using a tricky syntax
print(f"obj_myclass._Myclass__hiddenVariable = {obj_myclass._Myclass__hiddenVariable}")