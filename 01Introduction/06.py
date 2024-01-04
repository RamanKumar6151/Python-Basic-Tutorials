import os
os.system("cls")

lst=[1,2,3,4]
print(*lst)
tpl=(1,2,3,4)
print(*tpl)

# to parse or tom create extpression sin string
str=input("enter expression: ")
print(eval(str))

def fun():
    print("fun() function executed")

choice=input("enter the function name you want to execute ")
function_name=choice+"()"
eval(function_name)