'''Write a python program to import inbuilt modules such as math
and datetime.'''

import math, datetime

num = int(input("Enter A Number : "))
print(f"Square root : {math.sqrt(num)}")

print(f"Todays Date : {datetime.date.today()}")
print(f"Current Time : {datetime.datetime.now().time()}")