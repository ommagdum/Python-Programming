# Write a python program to demonstrate all string functions (len,join,split,replace,count,index,find changing cases) string slicing
# and string operations.

str1 = input("Enter A String : ")
print(f"Length Of String : {len(str1)}")

separate_str = {'TKIET', ', ', 'Warananagar'}
joined_str = ''.join(separate_str)
print(f"List of Words : {separate_str}")
print(f"After Join Operation : {joined_str}")

str2 = "Write A Python Program To Demonstrate String Functions."
print(f"String : {str2}")
print(f"After Split Operation : {str2.split()}")

str3 = str2.replace('Python','C')
print(f"Replacing 'Python' With 'C' In Previous String.")
print(f"String : {str3}")

Char = input("Enter A Character : ")
print(f"Occurances Of {Char} in Previous String : {str3.count(Char)}")
print(f"First Occurances Of {Char} in Previous String : {str3.index(Char)}")

print("Previous String In Lowercase : ")
print(f"{str3.lower()}")
print("Previous String In Uppercase : ")
print(f"{str3.upper()}")

print("Substring Of Previous String From (3 : 15)")
print(f"{str3[3:15]}")