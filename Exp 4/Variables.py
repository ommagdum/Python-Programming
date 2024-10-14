# Global variable
x = 10

def use_global():
    # Declare x as global to modify the global variable
    global x
    x = x + 5  # Modify global x
    print("Inside use_global, modified global x:", x)

def local_variable():
    # Local variable
    y = 20
    print("Inside local_variable, local y:", y)

def global_access():
    # Access global variable without modification
    print("Inside global_access, global x:", x)

# Calling functions
print("Global x before modification:", x)
use_global()  # modifies global x
local_variable()  # works with local variable y
global_access()  # accesses global x
print("Global x after modification:", x)