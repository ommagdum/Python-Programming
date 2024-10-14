# Student Information
name = "Om Magdum"
course = "TY B.Tech"
division = "B"
roll_no = 127

# a) Adding items 
original_tuple = (name, course, division, f"Roll no. {roll_no}")
print("Original Tuple:", original_tuple)

# Adding a new item to the tuple
new_item = "Age: 21"
updated_tuple = original_tuple + (new_item,)
print("Tuple after adding an item:", updated_tuple)

# b) Length of the tuple
print("Length of the original tuple:", len(original_tuple))

# c) Count occurrences of an item
count_division = original_tuple.count("B")
print("Count of 'B' in the tuple:", count_division)

# d) Find index of an item
index_course = original_tuple.index("TY B.Tech")
print("Index of 'TY B.Tech' in the tuple:", index_course)

# e) Sorted, Min, and Max (
numeric_tuple = (roll_no, 5, 3, 127, 10)
print("Numeric Tuple:", numeric_tuple)
print("Sorted Numeric Tuple:", sorted(numeric_tuple))
print("Minimum value in numeric tuple:", min(numeric_tuple))
print("Maximum value in numeric tuple:", max(numeric_tuple))

# f) Tuple Pack-Unpack
packed_tuple = (name, course, division, roll_no, new_item)
print("Packed Tuple:", packed_tuple)

# Unpacking the tuple
unpacked_name, unpacked_course, unpacked_division, unpacked_roll_no, unpacked_item = packed_tuple
print(f"Unpacked Tuple:\nName: {unpacked_name}\nCourse: {unpacked_course}\nDivision: {unpacked_division}\nRoll No: {unpacked_roll_no}\nAdditional Info: {unpacked_item}")

# g) Accessing tuple elements
print("First element of the tuple:", original_tuple[0])
print("Last element of the tuple:", original_tuple[-1])