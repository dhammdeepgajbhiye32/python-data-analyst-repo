# Here we will see how to create the dictonary in python.

# Syntax

# my_dict = {'Key1':'value1','key2':'value2','key3':'value3'....}

# method - 1: create dictionary by curley braces.

student = {
        "name" : "Madhav",
        "age" : 20,
        "city" : "Mathura" 
}

print(student)

# method - 2: create dictionary by using dictionary constructor.

per = dict(name = "madhav", age = 22,city = "Mumbai")
print(per)

# method - 3: create dictionary by using list of tuple.

person = dict([("name","Madhav"),("age",20),("city","mumbai")])
print(person)