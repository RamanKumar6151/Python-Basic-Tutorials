from os import system
system("cls")

"""
The walrus operator := is used for assignment within an expression. It allows you to assign a value to a variable as part of a larger expression. This can make the code more concise and readable in certain situations.
"""

# Without walrus operator
number = 10
if number > 5:
    print(f"{number} is greater than 5")

# With walrus operator
if (number := 10) > 5:
    print(f"{number} is greater than 5")

"""
In the second example, the walrus operator allows you to both assign the value 10 to the variable number and use it in the conditional expression number > 5 within the same line.

Another common use case is in while loops, where you want to both compute and use a value in the loop condition:
"""

# Without walrus operator
# data = get_data()
# while data is not None:
#     process_data(data)
#     data = get_data()

# With walrus operator
# while (data := get_data()) is not None:
#     process_data(data)


"""
In this case, the walrus operator eliminates the need to repeat the get_data() call and makes the code more concise.

In summary, the walrus operator is a tool for making your code more concise when you want to assign a value and use it within the same expression or statement. It's especially useful in conditions and loops.
"""
