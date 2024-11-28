'''Write a program that randomly generates a number. Raise a
user-defined exception if the number is below 0.1'''

import random


class MyError(Exception):
    def __init__(self, num, message = "Number Is Below 0.1"):
        self.num = num
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} Generated Number : {self.num}"
    
def RandNum():
    num = random.random()
    if num < 0.1:
        raise MyError(num)
    print(f"Generated Number : {num}")
    
try:
    while(True):
        RandNum()
except MyError as e:
    print(f"Error : {e.num} {e.message}")