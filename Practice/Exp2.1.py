'''Write a python program to enter any character. If the entered
character is in lowercase then convert it into uppercase and vice
versa'''

Char = input("Enter A Character (Alphabets Only) : ")
if (Char.islower()):
    print(f"Character in Uppercase : {Char.upper()}")
else:
    print(f"Character in Lowercase {Char.lower()}")