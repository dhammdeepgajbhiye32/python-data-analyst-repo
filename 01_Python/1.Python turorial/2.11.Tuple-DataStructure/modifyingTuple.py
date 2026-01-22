# Here we will see how to modify the value in tuple through converting tuple into list.

tuple_number = (1,2,5,8,9)
print(tuple_number)

# converting tuple into list.

list_number = list(tuple_number)
print(list_number)

list_number[0] = 100

print(list_number)

# converting list into tuple back

tuple_number = tuple(list_number)
print(tuple_number)