# Here we will see how to remove the key-value pair in dictionary in python.

student = {
    1 : "class-x",
    "name" : "madhav",
    "age" : 20,
    "email" : "madhav32@gmail.com"
}

# by using del method.

del student["age"]
print(student)

# by using remove with pop().

email = student.pop("email")
print(email)