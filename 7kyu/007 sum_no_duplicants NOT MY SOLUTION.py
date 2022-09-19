"""

Please write a function that sums a list, but ignores any duplicate items in the list.

For instance, for the list [3, 4, 3, 6] , the function should return 10.

"""

l = [1, 1, 2, 3]

def sum_no_duplicates(l):
    return sum(n for n in set(l) if l.count(n) == 1)

sum_no_duplicates(l)