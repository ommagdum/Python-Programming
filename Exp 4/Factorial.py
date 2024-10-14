# Iterative approach to find factorial
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Recursive approach to find factorial
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Lambda function to find factorial using reduce
from functools import reduce
factorial_lambda = lambda n: reduce(lambda x, y: x * y, range(1, n + 1), 1)

# Example usage
num = 5
print(f"Iterative factorial of {num}: {factorial_iterative(num)}")
print(f"Recursive factorial of {num}: {factorial_recursive(num)}")
print(f"Lambda factorial of {num}: {factorial_lambda(num)}")