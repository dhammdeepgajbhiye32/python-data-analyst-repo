# Print star pattern using loops.

n = int(input("Please enter the value of n:"))

for i in range(1, n+1):
    for j in range(1,i+1):
        print("*",end= " ")
    j+=1
    print()
i+=1
