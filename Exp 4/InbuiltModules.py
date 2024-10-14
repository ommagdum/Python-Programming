# Importing inbuilt modules
import math
import datetime

# Using math module
num = 9
print(f"Square root of {num}:", math.sqrt(num))
print(f"Factorial of {num}:", math.factorial(num))
print(f"Value of Pi:", math.pi)

# Using datetime module
current_date = datetime.date.today()
current_time = datetime.datetime.now().time()
print("Today's Date:", current_date)
print("Current Time:", current_time)