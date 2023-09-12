my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)

# for item in my_iterator:
#     print(item)

def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Create a generator object
my_generator = countdown(5)

try:
    while True:
        value = next(my_generator)
        print(value)
except StopIteration:
    pass

