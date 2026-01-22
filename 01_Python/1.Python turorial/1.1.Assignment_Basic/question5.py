# Admission Eligibility: A University has the following eligibility criteria for admission:
"""
1. Marks in Mathematics >= 65
2. Marks in Physics >= 55
3. Marks in chemistry >= 50
4. Total marks in all three subjects >= 180 Or Total marks in Mathematics and Physics >=140.

"""
# Write a program that takes marks in three sumbjects and prints whether the student is eligible for admission or not.

maths = int(input("Please enter the marks in Mathematics:"))
physics = int(input("Please enter the marks in Physics:"))
chemistry = int(input("Please enter the marks in Chemistry:"))

total = maths + physics + chemistry
print(f"the total marks obtained is: {total}")

if (maths >= 65) and (physics >= 55) and (chemistry >= 50) and (total >= 180) or (maths + physics >= 140):
    print("you are eligible for the addmission.")
else :
    print("you are not eligible for the addmission.")
