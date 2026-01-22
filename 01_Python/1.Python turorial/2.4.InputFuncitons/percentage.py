# Enter the name of the student and marks of 3 subjects
# and calculate the sum and percentage.

name = input("Please Enter the name of the Student.")
m1 = input("marks 1: ")
m2 = input("marks 2: ") 
m3 = input("marks 3: ")

sum = int(m1) + int(m2) + int(m3)
print(f"The total marks of 3 subjects is {sum}")

percentage = sum / 3

print(f"The percentage of the student is {int(percentage)}")