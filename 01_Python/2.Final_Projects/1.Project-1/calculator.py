# Here is the 1st project, which is a calculator by using function.

def addition(a,b):
    add = a + b
    return add
def subtraction(a,b):
    sub = a - b
    return sub
def multiplication(a,b):
    mul = a * b
    return mul
def division(a,b):
    div = a / b
    return div
def average(a,b): 
    avg = (a + b)/ 2
    return avg

print("Please select a operation: \n"\
        "1. Addition\n"\
        "2. Subtraction\n"\
        "3. Multiplication\n"\
        "4. Division\n"\
        "5. Averag\n")

a = int(input("Please enter the value of a:"))
b = int(input("Please enter the value of b:"))

select = int(input("Please select operation to perform:"))


if select == 1:
    add = addition(a,b)
    print(f"the sum is {add}")

elif select == 2:
    sub = subtraction(a,b)
    print(f"the minus is {sub}")

elif select == 3:
    mul = multiplication(a,b)
    print(f"the multiplication is{mul}")

elif select == 4:
    div = division(a,b)
    print(f"the div is {div}")

elif select == 5 :
    avg = average(a,b)
    print(f"the avg is {avg}")

else :
    print("invalid operation.")
