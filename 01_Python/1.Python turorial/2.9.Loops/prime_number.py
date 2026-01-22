# Here we will understand the prime number between 2 to 10 by using nested loop.

for i in range(2,10):
    for j in range(2,i):
        if(i % 2 == 0):
            break
        j+= 1
    else:
        print(i)