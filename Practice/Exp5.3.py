'''Find all of the numbers from 1-1000 that are divisible by 7,
using List Comprehension.'''

list1 = [x for x in range(1,1001) if x % 7 == 0]
print(f"Numbers From 1-1000 Divisible By 7 : {list1}")