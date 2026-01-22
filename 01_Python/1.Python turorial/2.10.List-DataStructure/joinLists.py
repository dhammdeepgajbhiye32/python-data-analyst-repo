# Here we will see the various methods to join more than two lists in python.

list1 = [1,2,'a','b']
list2 = [3,4,'c','d']

# 1st method is by using + operator.

list3 = list1 + list2
print(list3)

# 2nd method is by append

for x in list2:
    list1.append(x)
print(list1)

# 3rd method is by extend

list1.extend(list2)

print(list1)