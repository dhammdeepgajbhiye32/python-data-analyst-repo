# Create 2 sets with the names set1 and set2, where set1 contains the elements (1, 2, 3, 4, 5) and 
# set2 contains the elements (4, 5, 6, 7, 8). Perform the below operations and print the results:
# a) Union of set1 and set2
# b) Intersection of set1 and set2  
# c) Difference of set1 and set2 (set1 - set2)

# Define the sets

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)   

# a) Union of set1 and set2
union_set = set1.union(set2)

print("Union of set1 and set2:", union_set)
print()

# b) Intersection of set1 and set2
inter_set = set1.intersection(set2)

print("Intersection of set1 and set2:", inter_set)
print()

# c) Difference of set1 and set2 (set1 - set2)
diff_set = set1.difference(set2)
print("Difference of set1 and set2 (set1 - set2):", diff_set)
# set difference is the elements present in set1 but not in set2
print()