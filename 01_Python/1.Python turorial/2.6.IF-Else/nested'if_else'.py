# Here we will learn the use of nested if- else conditional statement.

num = int(input("Please enter any number."))

if num > 1 :
    if num % 2 == 0:
        print("The number is positive and even.")
    else :
        print("The number is positive and odd.")
else :
    if num == 0:
        print("The number is zero.")
    else : 
        print("The number is negative.")