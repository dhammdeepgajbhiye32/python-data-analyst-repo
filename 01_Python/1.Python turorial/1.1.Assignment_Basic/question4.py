# Login Authentication using conditional statement. Assume you have a predefined username and password.

# Write a program that prompts the user to enter a username and password and checks whether they match. Provide appropriate 
# messages for the following cases:
# 1. Both username and password are correct.
# 2. Username is correct but password is incorrect.
# 3. Username is incorrect.


username = "BK2195"
Password = "786971"

username1 = str(input("Please enter the UserName:"))
Password1 = str(input("Please enter the PassWord:"))

if (username == username1) and (Password == Password1):
    print("Both Username and Password ate correct.")
elif (username == username1) and (Password != Password1):
    print("Username is correct but Password is incorrect.")
else :
    print("Username is incorrect.")