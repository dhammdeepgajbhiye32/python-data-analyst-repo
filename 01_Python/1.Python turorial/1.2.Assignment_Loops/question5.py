# Printing First N Fibonaccie Numbers without while loop

N = int(input("Please enter the value:"))
a,b = 0,1
for i in range(N):
    print(a)
    a,b = b,a+b



# Write a program to print first N numbers in the fibonaccie series using a whlie loop

n = int(input("Please enter the value:"))

def fibonaccie_series (n):
    a,b = 0,1
    count = 0
    while(count < n):
        print(a)
        a,b = b,a+b
        count+=1

fibonaccie_series(n)


# Printing First N Fibonaccie Numbers for loop

n = int(input("Please enter the value:"))

def fibonaccie_series (n):
    a,b = 0,1
    for i in  range(n):
        print(a)
        a,b = b,a+b

# Printing First N Fibonaccie Numbers using Recursion

n = int(input("Please enter the value:"))

def fib (n):
    if n < 0:
        return "Invalid Input"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(n):
    print(fib(i))