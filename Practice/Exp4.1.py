'''Write a python program to create a tuple and perform the following
methods
a) Add items b) len c) count d) index e) sorted, min, max f) tuple pack-
unpack g) accessing tuple elements'''

name = 'Om Magdum'
RollNo = 127
Class = 'TY Btech'

tup1 = (name, RollNo, Class)
print(f"Intial Tuple : {tup1}")

Dep = 'CSE'
tup1 = tup1 + (Dep,)
print(f"Tuple After Adding Department : {tup1}")

print(f"Tuple Length : {len(tup1)}")
count_A = tup1.count("RollNo")
print(f"No. Occurances Of '127' in tuple : {count_A}")

pr