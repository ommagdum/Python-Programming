'''Write a python Program to read a number and display
corresponding day using if_elif_else?'''

num1 = int(input("Enter A Number : "))
print("Corresponding Day :")
if (num1 == 1):
    print("Monday")
elif(num1 == 2):
    print("Tuesday")
elif(num1 == 3):
    print("Wednesday")
elif(num1 == 4):
    print("Thursday")
elif(num1 == 5 ):
    print("Friday")
elif(num1 == 6):
    print("Saturday")
else:
    print("Sunday")