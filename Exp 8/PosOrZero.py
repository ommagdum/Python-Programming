# Write a program that prompts the user to enter a number. 
# If the number is positive or zero print it, otherwise raise an exception.

class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    pass

def check_number():
    try:
        number = float(input("Enter a number: "))
        if number < 0:
            raise NegativeNumberError("Negative numbers are not allowed.")
        else:
            print(f"The entered number is: {number}")
    except NegativeNumberError as e:
        print(e)

# Run the function
check_number()