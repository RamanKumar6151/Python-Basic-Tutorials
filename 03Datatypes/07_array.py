import os
import array as arr
os.system("cls")

# b,B-int(1 byte), 
# u-unicode character(2 byte)
# h,H,i,I- int(2 byte)
# L,q,Q-int (4 byte)
# f-float(4 byte)
# d-float(8 byte)

# array.array("datatype code",value_list)
# craeting an array
arr1=arr.array("i", [1,2,3,4,5,6])
print(type(arr1))
print(len(arr1))
for i in range(len(arr1)):
    print(arr1[i],end=" ")
print("\n")
for i in arr1:
    print(i,end=" ")