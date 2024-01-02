import os
os.system("cls")
# pyramid patterns
def pypart(n):
    # O(n^2)
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end=" ")
        print("\n")
def pypart_list(n):
    # O(n)
    lst=[]
    for i in range(1,n+1):
        lst.append("*"*i)
    print(" \n".join(lst))
pypart(5)
pypart_list(5)