import os
os.system("cls")
# returning multiple values
def fun():
    return 1,3 # will return the tuple(1,3)
print(fun())

# using lists
def fun2():
    return [1,3]
print(fun2())

# using yield
def fun3():
    yield 1
    yield 3
# for i in fun3():
#     print(i,end=" ")
# storing the object in temp
temp=fun3()
while(True):
    try:
        # converting the object into iterator and printing the values in it using __next__()
        print(iter(temp).__next__())
        # print(next(iter(temp)))
    except:
        break
