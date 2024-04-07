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