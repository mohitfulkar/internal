def divide(x, y): 
    try: 
        result = x / y 
    except ZeroDivisionError: 
        print("Error: Division by zero!") 
    else: 
        print(f"The result of {x} divided by {y} is {result}") 
    finally: 
        print("This will always execute, regardless of whether an exception occurred or not.") 
 
# Example usage 
print("Case 1:") 
divide(10, 2) 
print("\nCase 2:") 
divide(10, 0) 
print("\nCase 3:") 
try: 
    # This will raise a TypeError 
    divide(10, 'a') 
except Exception as e: 
    print(f"An error occurred: {e}") 