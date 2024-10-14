# Write a python program to create a set and perform the following methods :-a) add() (b) union() (c) intersection)
# d) difference) e) symmetric difference)

set1 = {1, 2, 3, 4, 5}
print(f"Set 1 : {set1}")
set1.add(6)
print("Adding 6 In Set 1")
print(f"Set 1 : {set1}")

set2 = {6, 7, 8, 9, 10}
print(f"Set 2 : {set2}")

union_set = set1.union(set2)
print(f"Union Of Set 1 & 2 : {union_set}")

inter_set = set1.intersection(set2)
print(f"Intersection Of Set 1 & 2 : {inter_set}")

diff_set = set1.difference(set2)
print(f"Difference Of Set 1 & 2 : {diff_set}")

sym_set = set1.symmetric_difference(set2)
print(f"Symmetric Difference Of Set 1 & 2 : {sym_set}")

set2.update(set1)
print(f"Updating Set 2 with Set 1 : {set2}")


