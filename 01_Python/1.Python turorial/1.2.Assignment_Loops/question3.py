# Print inverted triangle pattern by using loop.

n = int(input("Please enter the value of n:"))

for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*",end= " ")
        j -= 1
    print()
i -= 1