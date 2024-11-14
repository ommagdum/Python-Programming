def write_binary_file(filename, data):
    """Write data to a binary file."""
    with open(filename, 'wb') as file:
        file.write(data)
    print(f"Data written to {filename} in binary mode.\n")

def append_binary_file(filename, data):
    """Append data to a binary file."""
    with open(filename, 'ab') as file:
        file.write(data)
    print(f"Data appended to {filename} in binary mode.\n")

def read_binary_file(filename):
    """Read the content of a binary file."""
    with open(filename, 'rb') as file:
        content = file.read()
    print(f"Data read from {filename} in binary mode: {content}\n")

def read_and_write_binary_file(filename, data_to_write):
    """Read and write to a binary file."""
    with open(filename, 'rb+') as file:
        content = file.read()
        print(f"Data read from {filename} before writing: {content}")
        file.seek(0)  # Move to the beginning of the file to overwrite
        file.write(data_to_write)
    print(f"Data written to {filename} in binary mode.\n")

def append_and_read_binary_file(filename, data_to_append):
    """Append and read from a binary file."""
    with open(filename, 'ab+') as file:
        content = file.read()
        print(f"Data read from {filename} before appending: {content}")
        file.write(data_to_append)
    print(f"Data appended to {filename} in binary mode.\n")

# Define binary data
data = b"Hello, binary world!"
additional_data = b" Additional data."
file_name = "example_binary_file.dat"

# 1) Write binary data using 'wb' (overwrite mode)
write_binary_file(file_name, data)

# 2) Read binary data using 'rb'
read_binary_file(file_name)

# 3) Read and write binary data using 'rb+'
read_and_write_binary_file(file_name, additional_data)

# 4) Append binary data using 'ab'
append_binary_file(file_name, additional_data)

# 5) Append and read binary data using 'ab+'
append_and_read_binary_file(file_name, b" More appended data.")