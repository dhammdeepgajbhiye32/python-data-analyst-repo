# find the factorial of a number.

n = int(input("Please enter any value of n:"))

def fact(num):
        facto = 1
        while(num > 0):
                facto *= num
                num -= 1
        return facto

factorial = fact(n)

print(f"The factorial of a given number is: {factorial}")