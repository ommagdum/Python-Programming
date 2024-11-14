# Demonstrate read/readline/readlines and write/writeline/writelines in python.
# Creating a sample file for demonstration
filename = "demo.txt"

# Writing to the file using write() and writelines()
with open(filename, "w") as file:
    # write() writes a single string to the file
    file.write("Hello, World!\n")
    file.write("This is a demonstration file.\n")
    
    # writelines() writes a list of strings to the file
    lines = ["Line 1: This is the first line.\n", 
             "Line 2: This is the second line.\n", 
             "Line 3: This is the third line.\n"]
    file.writelines(lines)
print("File written successfully using write() and writelines().\n")

# Reading the file content using read(), readline(), and readlines()
with open(filename, "r") as file:
    print("Reading entire file content using read():")
    file_content = file.read()
    print(file_content)

with open(filename, "r") as file:
    print("Reading file line-by-line using readline():")
    line = file.readline()
    while line:
        print(line, end="")  # `end=""` to avoid double newlines
        line = file.readline()

with open(filename, "r") as file:
    print("\nReading all lines into a list using readlines():")
    lines = file.readlines()
    for line in lines:
        print(line, end="")