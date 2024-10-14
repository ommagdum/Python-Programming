# Given string
input_string = "warana university"

# Initialize an empty dictionary to store occurrences
letter_counts = {}

# Iterate over each character in the string
for letter in input_string:
    if letter != " ":  # Ignoring spaces
        # Convert to lowercase to make the count case-insensitive
        letter = letter.lower()
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

print("Number of occurrences of each letter:")
for letter, count in letter_counts.items():
    print(f"'{letter}': {count}")