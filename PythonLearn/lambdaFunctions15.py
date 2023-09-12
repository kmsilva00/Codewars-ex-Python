#lambda arguments: expression

# A lambda function that takes two arguments and returns their sum
add = lambda x, y: x + y

result = add(3, 4)  # Calling the lambda function
# result is 7







"""Sorting a List of Tuples by a Specific Element:

sorted(iterable, key=key, reverse=reverse)

"""
data = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
sorted_data = sorted(data, key=lambda x: x[1],reverse=False)  # Sort by the second element of each tuple

# print(sorted_data)


"""

Filtering a List:

filter(function, iterable)


"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# for i in even_numbers:
#     print(i)

"""

Mapping a List:

Applies a specified function to every item in an iterable (e.g., a list, tuple, or string) and return an iterator that yields the results

"""
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)

# for x in squared_numbers:
#     print(x)
    
words = ["apple", "banana", "cherry"]
uppercase_words = map(str.upper, words)
# uppercase_words is an iterator containing ["APPLE", "BANANA", "CHERRY"]

# for x in uppercase_words:
#     print(x)


list1 = [1, 2, 3]
list2 = [10, 20, 30]
list3 = [100, 200, 300]
result = map(lambda x, y, z: x + y + z, list1, list2, list3)
# result is an iterator containing [111, 222, 333]




"""Calculating the Sum Using reduce() (Python 3):"""
from functools import reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)

# print(total)
