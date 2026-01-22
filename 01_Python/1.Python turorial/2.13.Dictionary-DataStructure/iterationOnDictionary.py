# Here we will see how we can perform iteration on keys, values, and items in python.

student = {
    1 : "Class-X",
    "Name" : "Madhav",
    "Age" : 25,
    "Email" : "madhav32@gmail.com"
}

# performing iteration over key.

for key in student:
    print(key)

# performing iteration over value.

for value in student:
    print(student[value])

# performing itertion by using .value method.

for value in student.values():
    print(value)

# performing iteration by key-value pair method.

for key,value in student.items():
    print(key,value)