'''Write a python program to find largest number among three
numbers (using short hand if else).'''

num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))
num3 = int(input("Enter Number 3 : "))

print("Largest Number : ")
if (num1 > num2 and num1 > num3):
    print(f"Number 1 : {num1}")
elif(num2 > num3 and num2 > num3):
    print(f"Number 2 : {num2}")
else:
    print(f"Number 3 : {num3}")