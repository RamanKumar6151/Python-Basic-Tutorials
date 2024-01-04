# list comprehension
import os
os.system("cls")

import math

odd_square=[
    x**2
    for x in range(1,11)
    if x%2==1
]
print(odd_square)

power_of_2=[
    2**x
    for x in range(1,11)
]
print(power_of_2)

lst1=[
    2**x
    if(x%2==1)#if condition true 2**x will be inputed
    else x*2# else x*2 is inputed in list
    for x in range(1,10)
]
#for understanding ,above "lst" is same as below "lst1"
# lst1=[]
# for x in range(1,11):
#   if x%2==1:
#       lst1.append(x**2)
#   else:
#     lst1.append(x*2)
print(lst1)

# below list contains prime and non-prime in range 1 to 50 
x=2
non_primes=[
    j
    for i in range(2, int(math.sqrt(50))+1)
    for j in range(i*2, 50, i)
]
print(non_primes)
prime=[x for x in range(2,50) if x not in non_primes]
print(prime)

print([x.lower() for x in ['A','B','C']])
string="my phone number is : 2345677654 !!"
numbers=[int(x) for x in string if x.isdigit()]
print(numbers)

# list os list of multiplication table
a=5
table=[[a, b, a*b] for b in range(1,11)]
for i in table:
    print(i)