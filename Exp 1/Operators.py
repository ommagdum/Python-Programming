# Sample variables
a = 10
b = 3
x = True
y = False
list1 = [1, 2, 3]
list2 = [1, 2, 3]
str1 = "Python"

# 1. Arithmetic Operations
print("Arithmetic Operations:")
print("a + b =", a + b)  # Addition
print("a - b =", a - b)  # Subtraction
print("a * b =", a * b)  # Multiplication
print("a / b =", a / b)  # Division
print("a % b =", a % b)  # Modulus (remainder)
print("a ** b =", a ** b)  # Exponentiation (a raised to the power of b)
print("a // b =", a // b)  # Floor division (integer division)
print()

# 2. Relational (Comparison) Operations
print("Relational (Comparison) Operations:")
print("a == b:", a == b)  # Equal to
print("a != b:", a != b)  # Not equal to
print("a > b:", a > b)  # Greater than
print("a < b:", a < b)  # Less than
print("a >= b:", a >= b)  # Greater than or equal to
print("a <= b:", a <= b)  # Less than or equal to
print()

# 3. Logical Operations
print("Logical Operations:")
print("x and y:", x and y)  # Logical AND
print("x or y:", x or y)  # Logical OR
print("not x:", not x)  # Logical NOT
print()

# 4. Bitwise Operations
print("Bitwise Operations:")
print("a & b =", a & b)  # Bitwise AND
print("a | b =", a | b)  # Bitwise OR
print("a ^ b =", a ^ b)  # Bitwise XOR
print("~a =", ~a)  # Bitwise NOT
print("a << 2 =", a << 2)  # Left shift
print("a >> 2 =", a >> 2)  # Right shift
print()

# 5. Assignment Operations
print("Assignment Operations:")
c = 5
print("c =", c)  # Assign value
c += 2
print("c += 2 ->", c)  # Add and assign
c -= 2
print("c -= 2 ->", c)  # Subtract and assign
c *= 2
print("c *= 2 ->", c)  # Multiply and assign
c /= 2
print("c /= 2 ->", c)  # Divide and assign
c %= 2
print("c %= 2 ->", c)  # Modulus and assign
c **= 3
print("c **= 3 ->", c)  # Exponentiation and assign
c //= 2
print("c //= 2 ->", c)  # Floor division and assign
print()

# 6. Identity Operations
print("Identity Operations:")
print("list1 is list2:", list1 is list2)  # Checks if both variables point to the same object
print("list1 is not list2:", list1 is not list2)  # Checks if both variables do not point to the same object
print()

# 7. Membership Operations
print("Membership Operations:")
print("1 in list1:", 1 in list1)  # Checks if 1 is in list1
print("4 in list1:", 4 in list1)  # Checks if 4 is in list1
print("'P' in str1:", 'P' in str1)  # Checks if 'P' is in the string "Python"
print("'Z' not in str1:", 'Z' not in str1)  # Checks if 'Z' is not in the string "Python"