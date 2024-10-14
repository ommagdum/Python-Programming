# Input three numbers from the user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Finding the largest using shorthand if-else
largest = a if (a > b and a > c) else (b if b > c else c)

# Display the largest number
print(f"The largest number among {a}, {b}, and {c} is: {largest}")