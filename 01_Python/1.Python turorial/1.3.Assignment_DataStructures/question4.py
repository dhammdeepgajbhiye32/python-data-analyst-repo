# Create a dictionay with key value as 1,2,3 and the values as 'data','information',
# and 'text'. 
# a. After creating the dictionary, eliminate the 'text' value pair to the dictionary
# b. Add 'features' as value with key 4 to the dictionary.
# c. Print the updated dictionary and display the keys and values separately.

# Creating the dictionary
library = {
    1: 'data',
    2: 'information',
    3: 'text'
}

print("Original Dictionary:", library)
print()

# a. Eliminating the 'text' value pair
library.pop(3)

# Printing the dictionary after removal
print("After removing the key 3:", library)
print()

# b. Adding 'features' as value with key 4
library[4] = 'features'

# c. Printing the updated dictionary
print("Updated Dictionary:", library)



