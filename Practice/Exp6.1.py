'''Write a python program to demonstrate types of arguments.
(positional, keyword, default, variable length)'''

def student_info(name, div, dep = "CSE"):
    print(f"Name : {name}, Divison : {div}, Depatment : {dep}")

def course_info(course = 'Python', Year = 2024):
    print(f"Course : {course}, Year : {Year}")

def Hobbies(*hobbies_list):
    print(f"Hobbies : {hobbies_list}")

#Positional
student_info("Om Magdum", 'B')

#KeyWord
student_info(name="Om", div="B", dep="CSE")

#default 
course_info()

#variable
Hobbies("Coding", "Gaming", "Reading")