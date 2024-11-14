# Write a python class that has two methods: get_String and print_String, get_String accept a string from 
# the user and print_String prints the string in upper case.

class StringManipulator:
    def __init__(self):
        self.string = ""
    
    def get_String(self):
        self.string = input("Enter a string: ")
    
    def print_String(self):
        print(self.string.upper())

# Example usage
str_manipulator = StringManipulator()
str_manipulator.get_String()
str_manipulator.print_String()
