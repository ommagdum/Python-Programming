#Write a program to demonstrate input/output functions and type casting, in python.

num1 = int(input("Enter A Number : "))
print(f"Number : {num1}, Data Type : {type(num1)}")
num1 = float(num1)
print(f"After Typecasting : ")
print(f"Number : {num1}, Data Type : {type(num1)}")

num2 = float(input("Enter A Decimal Number : "))
print(f"Number : {num2}, Data Type : {type(num2)}")
num2 = int(num1)
print(f"After Typecasting : ")
print(f"Number : {num2}, Data Type : {type(num2)}")
