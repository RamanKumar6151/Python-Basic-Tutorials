import os
os.system("cls")
print(3 and 0)
# Apologies for the confusion in my previous responses. I made a mistake in my explanations.

# In Python, the `and` operator returns the first false operand or the last operand if both operands are true. If the first operand is true, it returns the second operand. If the first operand is false, it returns the first operand.

# Let's correct the explanation for the examples:

# 1. In `print(3 and 10)`, both `3` and `10` are true, so the `and` operator returns the second operand, which is `10`. Therefore, it prints `10`.

# 2. In `print(10 and 3)`, both `10` and `3` are true, so the `and` operator returns the second operand, which is `3`. Therefore, it prints `3`.

# I appreciate your patience, and I hope this clarifies the behavior of the `and` operator in Python.
print(3 and 10)
print(10 and 3)

# Certainly! In the context of the `or` operator in Python, it returns the first true operand or the last operand if both operands are false. If the first operand is true, it returns the first operand. If the first operand is false, it returns the second operand.

# Let's consider the examples:

# 1. In `print(3 or 10)`, both `3` and `10` are considered true in a boolean context. Therefore, the `or` operator returns the first operand, which is `3`. Therefore, it prints `3`.

# 2. In `print(10 or 3)`, both `10` and `3` are true, so the `or` operator returns the first operand, which is `10`. Therefore, it prints `10`.

# I hope this clears up any confusion.
print(3 or 0)
print(3 or 10)
print("\r")
# string is immutable , occupies same memory location
print('' is '')
# so is tuple
print(()is())
print((1)is(1))
# dictionary is mutable and occupy different memory location
print(type({}))
print({} is {})
# so is mutable list
print([] is [])
lst1=[1]
lst2=lst1
print(id(lst1)==id(lst2))  # will return true
lst2=[1]
print(id(lst1)==id(lst2))  # will return false
