try:
    num = int("abc")
except ValueError as e:
    print(f"error \n{e}\noccured")
    
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"error\n{e}\noccured")
    
try:
    num = int("abc")  # Raises a ValueError
    with open("nonexistent.txt", "r") as file:
        content = file.read()  # Raises a FileNotFoundError
except ValueError as ve:
    print(f"ValueError: {ve}")
except FileNotFoundError as fe:
    print(f"File not found: {fe}")
except Exception as e:
    print(f"An error occurred: {e}")
