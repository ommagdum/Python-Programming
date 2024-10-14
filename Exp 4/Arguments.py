# Function demonstrating types of arguments

# Positional and Keyword Arguments
def student_info(name, roll_no, division="B"):
    print(f"Name: {name}, Roll No: {roll_no}, Division: {division}")

# Default Arguments
def course_info(course="TY B.Tech", year=2024):
    print(f"Course: {course}, Year: {year}")

# Variable-Length Arguments
def hobbies(*hobby_list):
    print("Hobbies:", ", ".join(hobby_list))

# Function calls
# Positional Arguments
student_info("Om Magdum", 127)

# Keyword Arguments
student_info(name="Om Magdum", roll_no=127, division="B")

# Default Arguments
course_info()  # uses default values
course_info(course="B.Tech IT")

# Variable Length Arguments
hobbies("Coding", "Gaming", "Reading")