'''Reverse the string-
Input- “Warana University Warananagar”
Output-“anaraW ytisrevinU ragananaraW”'''

def reverse_string(s):
    s = s[::-1]
    return s

InputStr = input("Enter A String : ")
reversed_string = reverse_string(InputStr)
print(f"Reversed String : '{reversed_string}'")