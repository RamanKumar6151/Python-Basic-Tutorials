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
# Outer Loop (for i in range(2, int(math.sqrt(50)) + 1):

# The outer loop iterates over the numbers i from 2 to the square root of 50 (rounded up to the nearest integer). The purpose of this loop is to iterate through potential prime numbers.
# The use of int(math.sqrt(50)) + 1 is a common optimization technique. It's based on the fact that if a number n is not a prime, it must have a factor less than or equal to its square root. So, iterating up to the square root is sufficient to find potential factors.
# Inner Loop (for j in range(i * 2, 50, i):

# The inner loop generates multiples of the current i. It starts from i * 2 (the first multiple of i greater than or equal to 4) and goes up to 50, incrementing by i each time.
# The purpose of this inner loop is to identify and mark the multiples of i as non-prime numbers. If i is a prime number, its multiples will be non-prime.
# List Comprehension (j for i in ... for j in ...):

# The list comprehension collects all the identified non-prime numbers (j) into the non_primes list.
# It essentially flattens the nested loop structure into a single list.
# Reasoning:

# The approach of marking multiples of prime numbers is a common technique used in the Sieve of Eratosthenes algorithm, which is an efficient algorithm for finding all primes up to a given limit.
# By eliminating the multiples of each potential prime number, the code efficiently identifies non-prime numbers within the specified range.
# Example:

# Let's take i = 2. The inner loop generates multiples starting from 2 * 2 (4) up to 50, incrementing by 2 each time. So, it marks 4, 6, 8, 10, ..., 50 as non-prime.
# The process continues for subsequent values of i, marking multiples and eliminating non-primes.
# The overall result is a list of non-prime numbers up to 50. This method is particularly useful for efficiently identifying non-primes within a range by leveraging the properties of prime numbers and their multiples.
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