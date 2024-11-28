'''Write a python program to find factorial of a given number using
functions (iterative, recursive) and also demonstrate lambda
function.'''

def fact_itr(num):
    result = 1
    if num == 0 or num == 1:
        return 1
    for i in range(1, num+1):
        result *= i
    return result

def fact_rec(num):
    if num == 0 or num == 1:
        return 1
    return num * fact_rec(num - 1)

num = int(input("Enter A Number : "))
from functools import reduce
fact_lambda = lambda num: reduce(lambda x, y: x * y, range(1, num + 1),1)
print(f"Factotial By Iterative Method : {fact_itr(num)}")
print(f"Factotial By Iterative Method : {fact_rec(num)}")
print(f"Factotial By Lambda Method : {fact_lambda(num)}")