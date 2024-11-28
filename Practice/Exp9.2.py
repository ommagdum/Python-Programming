'''Demonstrate read/readline/readlines and
write/writeline/writelines in python.'''

with open("Sample.txt",'r') as file:
    content = file.read()
    print(content)
    FirstLine = file.readline()
    print(FirstLine)
    RemainingLines = file.readlines()
    print(RemainingLines)

with open("new_text.txt",'w') as file:
    file.write("This Is First Line")
    lines = ['This Is Second Line\n', 'This Is Third Line\n']
    file.writelines(lines)
