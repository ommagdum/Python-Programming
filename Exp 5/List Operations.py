''' Write a python program to create a list and perform the following methods :-a) insert () b) remove () c) append ()
d) len() e) pop() (f) extend()(g) reverse() (h)sort()'''

list1 = [10, 20, 30, 40, 50]
print(f"Initial List : {list1}")

# Insert
list1.insert(5,60)
print("Inserting Element 60 : ")
print(f"Updated List : {list1} ")

# Remove
list1.remove(60)
print("Removing Element 60 : ")
print(f"Updated List : {list1} ")

# Append
list1.append(60)
print("Appending Element 60 : ")
print(f"Updated List : {list1} ")

# Length
print(f"Size Of List : {len(list1)} ")

# Pop
list1.pop()
print("Popping Last Element : ")
print(f"Updated List : {list1} ")

# Extend
list2 = [60, 70, 80, 90, 100]
list1.extend(list2)
print("Joining Two Lists : ")
print(f"Updated List : {list1} ")

# Reverse
list1.reverse()
print("Reversing List : ")
print(f"Updated List : {list1} ")

# Sort
listUnsorted = [43, 484, 82, 12, 48]
print(f"Unsorted List : {listUnsorted}")
listUnsorted.sort()
print(f"List After Sorting : {listUnsorted}")
