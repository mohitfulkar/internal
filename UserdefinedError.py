# Define a custom exception class 
class MyCustomException(Exception): 
    def __init__(self, message="This is a custom exception."): 
        self.message = message 
        super().__init__(self.message) 
 
# Function that raises the custom exception 
def my_function(x):
    if x < 0: 
        raise MyCustomException("Number should be non-negative.") 
    else: 
        print("Number is valid.") 
 
# Example usage 
try: 
    num = int(input("Enter a number: ")) 
    my_function(num) 
except MyCustomException as e: 
    print(f"Custom Exception Caught: {e}") 