# Write a program that perform file handling operations 
# 1) open 2) read 3) write 4) close 5) append

def open_file(filename, mode):
    """Open a file in the given mode and return the file object."""
    try:
        file = open(filename, mode)
        print(f"File '{filename}' opened in {mode} mode.")
        return file
    except Exception as e:
        print(f"Error opening file: {e}")
        return None

def read_file(file):
    """Read and print the contents of the file."""
    try:
        content = file.read()
        print("File contents:")
        print(content)
    except Exception as e:
        print(f"Error reading file: {e}")

def write_to_file(file, text):
    """Write the given text to the file."""
    try:
        file.write(text)
        print("Text written to file.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def append_to_file(file, text):
    """Append the given text to the file."""
    try:
        file.write(text)
        print("Text appended to file.")
    except Exception as e:
        print(f"Error appending to file: {e}")

def close_file(file):
    """Close the file."""
    try:
        file.close()
        print("File closed.")
    except Exception as e:
        print(f"Error closing file: {e}")

# File handling operations
filename = "example.txt"

# 1) Open the file in write mode to create it or overwrite it
file = open_file(filename, "w")
if file:
    write_to_file(file, "This is the initial content.\n")  # 3) Write to the file
    close_file(file)  # 4) Close the file

# 2) Open the file in read mode and read its contents
file = open_file(filename, "r")
if file:
    read_file(file)  # Read the file
    close_file(file)  # Close the file

# 5) Open the file in append mode and add more content
file = open_file(filename, "a")
if file:
    append_to_file(file, "This line is appended to the file.\n")  # Append to the file
    close_file(file)  # Close the file

# Re-open in read mode to verify the append operation
file = open_file(filename, "r")
if file:
    read_file(file)
    close_file(file)