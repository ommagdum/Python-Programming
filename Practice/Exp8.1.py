'''Write a program that prompts the user to enter a number. If
the number is positive or zero print it, otherwise raise an
exception.'''

try:
    num = int(input("Enter A Number : "))
    if num < 0:
        raise ValueError("Entered Number Is Negative.")
    
    print(f"Entered Number : {num}")

except ValueError as e:
    print(f"Error : {e}")