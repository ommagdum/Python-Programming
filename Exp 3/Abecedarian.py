# Function to check if the string is Abecedarian
def is_abecedarian(s):
    s = s.upper()  # Convert to uppercase to handle case insensitivity
    return s == ''.join(sorted(s))

# Example usage
input_string = input("Enter a string: ")

if is_abecedarian(input_string):
    print(f"'{input_string}' is an Abecedarian series.")
else:
    print(f"'{input_string}' is not an Abecedarian series.")