# Here we will see different types to create tuple in python.

# 1. By using parenthesis.

# tuple = (1,2,3,4,5)
# print(tuple)

# 2. By without parenthesis.

tuple1 = 1,3,4,5,7
print(tuple1)

# 3. By using tuple constructor()

tuple2 = tuple((1,5,8,9))
print(tuple2)

# 4. By passing list in tuple constructor()

list = [1,2,3,4,5]
new_tuple = tuple((list))
print(new_tuple)

# 5. Making a single element tuple.

a = ("a",)
print(type(a))  # so by adding a comma it becomes tuple/
print(a)