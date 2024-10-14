# a) Creating the dictionary with student information
student_dict = {
    "Name": "Om Magdum",
    "Course": "TY B.Tech",
    "Division": "B",
    "Roll_no": 127
}

# b) Print the dictionary items
print("Student Dictionary:", student_dict)

# c) Access items
print("Accessing Name:", student_dict["Name"])

# d) Get method
print("Get Course:", student_dict.get("Course"))

# e) Length of the dictionary
print("Number of items in dictionary:", len(student_dict))

# f) Add elements into an empty dictionary
empty_dict = {}
empty_dict["Hobby"] = "Coding"
empty_dict["City"] = "Sangli"
print("Empty Dictionary after adding elements:", empty_dict)

# g) Clear method
student_dict.clear()
print("Student Dictionary after clearing:", student_dict)

# Re-initialize the dictionary for further operations
student_dict = {
    "Name": "Om Magdum",
    "Course": "TY B.Tech",
    "Division": "B",
    "Roll_no": 127
}

# h) Pop an element
popped_item = student_dict.pop("Division")
print(f"Popped item 'Division': {popped_item}")
print("Dictionary after popping 'Division':", student_dict)

# i) Keys and Values
print("Dictionary Keys:", student_dict.keys())
print("Dictionary Values:", student_dict.values())

# j) Items
print("Dictionary Items:", student_dict.items())

# k) Copy the dictionary
copied_dict = student_dict.copy()
print("Copied Dictionary:", copied_dict)

# l) Update the dictionary
student_dict["Age"] = 21
print("Dictionary after adding 'Age':", student_dict)

# m) Merging two dictionaries
personal_info = {
    "City": "Sangli",
    "Hobby": "Coding"
}

# Method 1: Using update()
merged_dict = student_dict.copy()  # To keep the original student_dict intact
merged_dict.update(personal_info)
print("Merged Dictionary using update():", merged_dict)
