# Find the Intersection (common elements) of two lists.

# 1st methoda

l1 = [1,3,4,5]
l2 = [3,4,6,7,8]

set1 = set(l1)
set2 = set(l2)

set3 = set1.intersection(set2)

l3 = list(set3)

print(l3)

# 2nd method.

l1 = [1,2,3,4,5]
l2 = [4,5,6,7,8]

def intersection(list1,list2):
    return[item for item in l1 if item in l2]

print(intersection(l1,l2))