# Here we will learn the use of loops for iterating the tupples in python.

# 1. by using for loop.

tuple = ("apple","banana","cherry","blueberry")

for i in tuple:
    print(i,end=" ")

# 2. by while loop.

tuple = ("apple","banana","cherry","blueberry")
i = 0
while(i < len(tuple)):
    print(tuple[i])
    i+=1