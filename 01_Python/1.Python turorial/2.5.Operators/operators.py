# # Here we will learn about the Operators present
# # in the Python Programming Language.


# 1. Arithmetic Operators

a = 5
b = 3

print(a + b)    # addition operator
print(a - b)    # subtraction operator
print(a * b)    # multiplication operator
print(a / b)    # division operator

# 2. Comparision Operator- output is boolean value( True / False )

a = 5
b = 3

print( a > b) # output = True
print( a < b) # output = False
print( a == b) # output = False
print( a != b) # output = True

# 3. Assignment Operator

a = 5 # assignment operator.

# 4. Logical Operators

a = 10
b = 30

print( a > 10 and b < 40) # output = False
print( a > 10 or b < 40) # output = True
print( a < 20 | b > 40) # output = False

# 5. Identity Operators - is, is not

x = [1,2,3]
y = x
z = [1,2,3]

print(x is y) # output = True
print(x is z) # output = False

print(x is not z) # output = True

# 6. Membership Operators - in, not in

myList = ['apple','mango','watermellon']
print('apple' in myList) # output = True
print('apple2' in myList) # output = False
print('apple'  not in myList) # output = False
print('apple2' not in myList) # output = True

# 7. Bitwise Operators - AND, OR, XOR, NOT, etc

a = 5  # binary number = 0101
b = 3  # binary number = 0011

print(a & b) # output = 0001 = 1
print(a | b) # output = 0111 = 7
print(a ^ b) # output = 0110 = 6
print(~ b) # output = 1100 = -4

