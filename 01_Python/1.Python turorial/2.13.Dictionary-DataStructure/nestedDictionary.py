# Here we will see how nested dictionary actiyally works in python.

students ={ "student1" : {
    "name": "madhav",
    "age" : 21,
    " grade" :"A"},
    "student2" : {
    "name" : "keshav",
    "age" : 24,
    "grade" : "B"
    }
}

print(students["student1"]["name"])