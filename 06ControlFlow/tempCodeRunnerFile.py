import os
os.system("cls")

# looping techniques
# enumerate()
lst=list("geeks")
for i,v in enumerate(lst):
    print(i,v,sep="=")
dct={"a":1, "b":2, "c":3}
for k in dct:
    print(k,dct[k],sep="=")

