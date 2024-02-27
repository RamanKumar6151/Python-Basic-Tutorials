from os import system
from operator import add, iadd
system("cls")

print("inplace operator\n")
"""
In Python, inplace operators are a concise way of performing an operation and updating the value of a variable in place. They combine an operation with an assignment. Instead of using the traditional form a = a + b, inplace operators allow you to write a += b, making the code more concise.

Here are some common inplace operators:

+=: In-place addition
-=: In-place subtraction
*=: In-place multiplication
/=: In-place division
%=: In-place modulus
**=: In-place exponentiation
//=: In-place floor division
"""
a=5
b=3
a+=b
print(f"a={a}")  # Ouptut: a=8
"""
These operators are commonly used when you want to update the value of a variable based on its current value and the result of an operation. They are more concise than writing out the full assignment statement.

It's important to note that not all data types support all inplace operators. For instance, they work well with mutable objects like lists, but for immutable objects like INTEGERS or STRINGS, A NEW OBJECT IS CREATED, AND THE VARIABLE IS REASSIGNED.
"""

# mutable objects like list
print("\nmutable objects like list")
my_list=[1,2,3]
my_list+=[4,5,6]
print("my_list=", my_list)

# immutable object like strings
print("\nimmutable object like strings")
my_string="Hello"
my_string+=" world"
print("my_string=", my_string)

"""
The `operator.add()` function in Python is a built-in function provided by the `operator` module. It is equivalent to the `+` operator and is used to perform addition on two operands.

Here's the basic syntax of `operator.add()`:

```python
operator.add(a, b)
```

- `a` and `b`: The two operands that you want to add.

This function is useful when you need to perform addition programmatically and want to use a function instead of the `+` operator directly. It can be particularly handy when working with higher-order functions or when passing a function as an argument to another function.

Here's an example:
"""
result = add(3, 4)
print(result)  # Output: 7

"""
In this example, `operator.add(3, 4)` is equivalent to `3 + 4`, and the result is `7`.

While `operator.add()` is useful in certain situations, in most cases, you can use the `+` operator directly for addition, and it's more common to see the operator used in this way.

"""
result = 3 + 4
print(result)  # Output: 7
"""
Use `operator.add()` when you need to pass an addition function as an argument or when using it in a more dynamic or functional programming context. Otherwise, the `+` operator is more commonly used for simplicity and readability.
"""

"operator.iadd() is also used forr inplace addition"
print("\noperator.iadd(target, value)")
new_list=[1,2,3]
iadd(new_list, [4,5,6])
print(new_list)
# iadd() doesnt worls like above in case of immutable objects