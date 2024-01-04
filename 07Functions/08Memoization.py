import os
os.system("cls")

# memoiziation: technique to store intermediate result
# to avoid unnecesaary repeated calculations during recursion

print("memoiziation\n")

# using decorator to implement memoiziation
memory={}
def memorize_factorial(f):
    # have access to num, f
    def inner(num):
        if num not in memory:
            memory[num]=f(num)
            print("saving result in memory")
        else:
            print("returning result from memory")
        return memory[num]
    # returning the object
    return inner

@memorize_factorial
# recursive function for factorial
def factorial(num:int)->int:
    if num==1:
        return 1
    else:
        return num*factorial(num-1)
    
print(f"factorial(5)= {factorial(5)}")
print(f"factorial(5)= {factorial(5)}")

print(f"\nmemory={memory}\n")

# this will allow me to get result without calculation if it have been calculated once before

# like factorial(4)
print(f"factorial(4)={factorial(4)}")