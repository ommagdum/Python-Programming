# Initial sets
set1 = {"Om", "Magdum", "TY B.Tech", "Roll no. 127"}
set2 = {"Division B", "Coding", "Om"}

# Update set1 with items that don't exist in set2
set1.difference_update(set2)
print("Set1 after updating with items that don't exist in Set2:", set1)