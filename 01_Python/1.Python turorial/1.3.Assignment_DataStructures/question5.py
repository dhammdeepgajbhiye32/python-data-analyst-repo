# Creating a tuple with elements 1,2,3,apple,mango in my_tuple.

my_tuple = (1,2,3,'apple','mango')

print("Original Tuple:", my_tuple)


# Create a new tuple with named numeric_tuple consistion of only integer values
# 10,20,30,40,50. 
# a. Find the minimum and maximum value from the tuple.
# b. Concatenate the numeric_tuple with another tuple named new_tuple and result in t1.
# c. Duplicate the numeric_tuple twice and store it in 'newdupli'.

# Creating the numeric_tuple
numeric_tuple = (10,20,30,40,50)

print("Numeric Tuple:", numeric_tuple)

# a. Finding the minimum and maximum value from the tuple
min_value = min(numeric_tuple)
max_value = max(numeric_tuple)

print("Minimum Value:", min_value)
print()
print("Maximum Value:", max_value)  
print()

# b. Concatenating the numeric_tuple with another tuple named my_tuple and result in t1

t1 = my_tuple + numeric_tuple
print("Concatenated Tuple (t1):", t1)
print()

# c. Duplicating the numeric_tuple twice and store it in newdupli
newdupli = my_tuple * 2
print("Duplicated Tuple (newdupli):", newdupli)