import os
os.system("cls")
# switch case
# instead of swith case we have match: case :
# only works in version 3.10.1 or more
def fun(arg):
    match arg:
        case 0:
            return "zero"
        case 1:
            return "one"
        case default:
            return "default case"

arg=int(input("enetr num : "))
print(f"match case {fun(arg)}")