# Here we need to check that the entered year is the leap year or not.

year = int(input("Please enter any year:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"The {year} is a leap year.")
else :
    print(f"The {year} is not a leap year.")