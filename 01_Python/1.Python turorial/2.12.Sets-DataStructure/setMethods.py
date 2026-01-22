# Here we will see various methods present in the set in python.

# 1. union method.

set_a = {1,2,3}
set_b = {3,4,5}

union_set = set_a.union(set_b)
print(union_set)

# 2. intersection method.

set_a = {1,2,3}
set_b = {3,4,5}

intersection_set = set_a.intersection(set_b)
print(intersection_set)

# 3. difference method.

set_a = {1,2,3}
set_b = {3,4,5}

difference_set = set_a.difference(set_b)
print(difference_set)

# 4. symmetric difference method.

set_a = {1,2,3}
set_b = {3,4,5}

set_differnce_set = set_a.symmetric_difference(set_b)
print(set_differnce_set)