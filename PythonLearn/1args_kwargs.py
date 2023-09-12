"""
args = pass TUPLE as input of fn
kwargs = pass dictionary as input of fn

*args allows the user to pass a variable number of positional arguments, which are collected into a tuple inside the function.

**kwargs allows the user to pass a variable number of keyword arguments (key-value pairs), which are collected into a dictionary inside the function.
"""

# *args (Arbitrary Positional Arguments)
"""The *args syntax allows you to pass a variable number of non-keyword (positional) arguments to a function. 
It collects these arguments into a tuple."""

def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum_all(1, 2, 3, 4, 5)
print(result)  # Output: 15


#**kwargs (Arbitrary Keyword Arguments)
""" The **kwargs syntax allows you to pass a variable number of keyword arguments (key-value pairs) to a function. 
It collects these arguments into a dictionary."""

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, city="New York")

