import os
os.system("cls")

# __iter__() ad __next__()
# converting the object into an iterator
# iter() converts object into iterator
# next() or iterator.__next__(access the elements of iterator
# raises StopIterationError when all elements have been iterated
lst=[1,2,3,4]
iter_lst=iter(lst)
# try:
#     print(next(iter_lst))
#     print(next(iter_lst))
#     print(next(iter_lst))
#     print(next(iter_lst))
# except:
#     pass
while(True):
    try:
        print(iter_lst.__next__())
    except:
        break

# working with iterator using oops.....