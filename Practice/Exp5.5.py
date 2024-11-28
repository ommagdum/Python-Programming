'''Update the first set with items that don’t exist in the second
set.'''

set1 = {1, 2, 3, 4, 5, 6}
set2 = {3, 4, 5, 6, 7, 8, 9, 10}

for i in set1:
    for j in set2:
        if j is not i:
            set1.add(j)

print(set1)