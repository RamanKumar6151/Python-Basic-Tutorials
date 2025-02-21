# itertools
import os
os.system("cls")

import itertools
print("INFINITE ITERATORS")
print("1. itertools.count(start,step)")
# itertools.count(start,stop) create a infinite iteration starting with'start' and jumps 'step"
for i in itertools.count(5,5):
    if i>35:
        break
    else:
        print(i,end=" ")

print("\n2. itertools.cycle(iterable)")
# itertools.cycle(iterable) prints all value in order from the passed container, 
# starts printing from beginning again when all elements are printed in cyclic manner
count=0
for i in itertools.cycle("AB"):
    if count>7:
        break
    else:
        print(i, end=" ") 
        count=count+1

print("\n3. using next() function")
lst=["geeks", "for", "geeks"]
# defining iterator
iterator= itertools.cycle(lst)
print(iterator)
# will start printing infinetly
# for i in iterator:
#     print(i, end=" ")

for i in range(6):
    print(next(iterator), end=" ")

print("\n4. itertools.repeat(val,num)")
# repeats val infinte number of times
# if num is given then repeats num number of times
print(list(itertools.repeat(25,4)))

print("\nCOMBINATORIC ITERTOR")
# recursive generators that compute cartesian product, permutaions, combinations are called cominatoric iterators
print('1. ietertools.product(iterable, repeat=num)')
# computes the cartesian product of iterable with itself
# optional repeat keyword defimees the number of repetetitions
print(list(itertools.product([1,2], repeat=2))) 

print("2. itertools.permutation()")
# i dont want to study it for now, its getting more and more complex
