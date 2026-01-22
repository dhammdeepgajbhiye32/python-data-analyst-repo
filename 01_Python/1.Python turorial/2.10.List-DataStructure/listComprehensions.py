# Here we will see the use of comprehensions used in list in python.

# 1st creating the list of squares.

list = [x ** 2 for x in range(1,6)]
print(list)


# 2nd filtering even numbers.

list1 = [x for x in range(1,11) if x % 2 == 0]
print(list1)

# 3rd Applying a function to each element.

fruits= ["apple","banana","cherry","blueberry"]

uppercase_fruit = [fruit.upper() for fruit in fruits]
print(uppercase_fruit)