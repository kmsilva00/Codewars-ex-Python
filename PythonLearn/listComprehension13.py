squares = [x**2 for x in range(10)]
# Result: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squarescon = [x**2 for x in range(10) if x%3 == 0]
# Result: [0, 9, 36, 81]

words = ["apple", "banana", "cherry", "date", "elderberry"]
long_words = [word for word in words if len(word) > 5]
# Result: ["banana", "cherry", "elderberry"]

nested_lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
flat_list = [item for sublist in nested_lists for item in sublist]
# Result: [1, 2, 3, 4, 5, 6, 7, 8]


names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]
student_data = [(name, score) for name, score in zip(names, scores)]
# Result: [("Alice", 95), ("Bob", 87), ("Charlie", 92)]

