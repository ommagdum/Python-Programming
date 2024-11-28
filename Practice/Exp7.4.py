'''Write a python class that has two methods: get_String and
print_String, get_String accept a string from the user and print_String
prints the string in upper case.'''

class StrClass:

    def get_String(self):
        self.str1 = input("Enter A String : ")

    def print_String(self):
        print(f"{self.str1.upper()}")

ob1 = StrClass()
ob1.get_String()
ob1.print_String()