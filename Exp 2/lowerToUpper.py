# Function to change case of the entered character
def change_case(char):
    if char.islower():
        return char.upper()
    elif char.isupper():
        return char.lower()
    else:
        return "Invalid input, please enter an alphabet character."

# Input a character from the user
char_input = input("Enter a character: ")

# Check if input is a single alphabet character
if len(char_input) == 1 and char_input.isalpha():
    result = change_case(char_input)
    print("Converted character:", result)
else:
    print("Please enter a valid single alphabet character.")