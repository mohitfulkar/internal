# 1. SyntaxError 
# This line will raise a SyntaxError because of the missing closing 
parenthesis 
# print("Hello, world!" 
 
try: 
    print("Hello, world!") 
except SyntaxError as e: 
    print(f"SyntaxError: {e}") 
 
# 2. TypeError 
# Trying to concatenate a string with an integer will raise a TypeError 
try: 
    result = "Hello" + 42 
except TypeError as e: 
    print(f"TypeError: {e}") 
 
# 3. IndexError 
# Trying to access an index that doesn't exist in a list will raise an 
IndexError 
try: 
    my_list = [1, 2, 3] 
    print(my_list[5]) 
except IndexError as e: 
    print(f"IndexError: {e}") 
 
# 4. ValueError 
# Trying to convert a string that cannot be converted to an integer will raise 
a ValueError 
try: 
    num = int("hello") 
except ValueError as e: 
    print(f"ValueError: {e}") 
 
# 5. ZeroDivisionError 
# Division by zero will raise a ZeroDivisionError 
try: 
    result = 10 / 0 
except ZeroDivisionError as e: 
    print(f"ZeroDivisionError: {e}") 
 
# 6. FileNotFoundError 
# Trying to open a file that doesn't exist will raise a FileNotFoundError 
try: 
    with open("nonexistent_file.txt", "r") as file: 
        content = file.read() 
except FileNotFoundError as e: 
    print(f"FileNotFoundError: {e}")