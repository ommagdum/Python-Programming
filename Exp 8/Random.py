# Write a program that randomly generates a number. 
# Raise a user-defined exception if the number is below 0.1 
import random

class NumberTooLowError(Exception):
    """Custom exception raised when the number is below 0.1."""
    pass

def generate_and_check_number():
    number = random.random()  # Generates a random number between 0 and 1
    print(f"Generated number: {number}")
    
    if number < 0.1:
        raise NumberTooLowError("The generated number is below 0.1.")
    else:
        print("The generated number is acceptable.")

# Run the function and handle the custom exception
try:
    generate_and_check_number()
except NumberTooLowError as e:
    print(e)