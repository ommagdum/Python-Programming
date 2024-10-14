# 3.Write a program to demonstrate input/output functions and type casting in python.

var1 = int(input("Enter A Integer : "))
var1 = float(var1)
print("Typecasting Integer -> Float")
print(f"Value : {var1} Data Type : {type(var1)}")

var2 = float(input("Enter A Decimal : "))
var2 = int(var2)
print("Typecasting Float -> Integer")
print(f"Value : {var2} Data Type : {type(var2)}")

