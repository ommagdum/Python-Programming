# Sample string
sample_string = "Hello, Warana University!"

# 1. len() - Get the length of the string
print("Length of the string:", len(sample_string))

# 2. join() - Join elements of a list into a string
words_list = ['Hello', 'from', 'Warana', 'University']
joined_string = ' '.join(words_list)
print("Joined string:", joined_string)

# 3. split() - Split a string into a list
split_string = sample_string.split()  # Split by space by default
print("Split string:", split_string)

# 4. replace() - Replace a substring with another string
replaced_string = sample_string.replace("Warana", "XYZ")
print("String after replacement:", replaced_string)

# 5. count() - Count occurrences of a substring
count_of_a = sample_string.count("a")
print("Count of 'a' in the string:", count_of_a)

# 6. index() - Find the index of the first occurrence of a substring
index_of_university = sample_string.index("University")
print("Index of 'University' in the string:", index_of_university)

# 7. find() - Find the index of a substring (returns -1 if not found)
find_result = sample_string.find("Warana")
print("Find result for 'Warana':", find_result)

# 8. Accessing characters by index
first_char = sample_string[0]  # First character
last_char = sample_string[-1]  # Last character
print(f"First character: {first_char}, Last character: {last_char}")

# 9. String slicing - Accessing a part of the string
substring = sample_string[7:13]  # Slicing from index 7 to 12
print("Substring (7:13):", substring)

# 10. String operations (concatenation and repetition)
greeting = "Hello"
location = "Warana University"
concatenated_string = greeting + " " + location  # Concatenation
repeated_string = greeting * 3  # Repetition
print("Concatenated string:", concatenated_string)
print("Repeated string:", repeated_string)

# 11. Changing case
upper_case_string = sample_string.upper()  # Convert to uppercase
lower_case_string = sample_string.lower()  # Convert to lowercase
print("Uppercase string:", upper_case_string)
print("Lowercase string:", lower_case_string)

# 12. Strip - Remove leading/trailing whitespace
string_with_spaces = "  Hello, Warana!   "
stripped_string = string_with_spaces.strip()
print("String after stripping spaces:", stripped_string)