# Here we will make a password strength checker.

import re

# Password should be minimum of 8 characters
# It should contain digit, upper case characters,
# lower case characters, special characters.

def password_strenght_checker(password):
    if len(password) < 8:   # length of the password
        return "weak: Password must be atleast 8 characters."
    
    if not any(char.isdigit() for char in password):
        return "weak: Password must have alteast 1 digit."

    if not any(char.isupper() for char in password):
        return "weak: Password must have atleast 1 uppercase character."
    
    if not any(char.islower() for char in password):
        return "weak: Password must have atleast 1 lowercase character."
    
    if not re.search(r'[~!@#$%^&*():;<>,.?/|]',password):
        return "medium: Password must have atleast 1 special character."

    return "Strong: Your Password is strong and Secured."

def password_checker():
    print("Welcome to the Password Strenght Checker:")

    while True:
        password = input("enter your password ( or type 'exit' to quit):")

        if password.lower() == 'exit':
            print("Thankyou for using this tool")
            break
 
        result = password_strenght_checker(password)
        print(result)


# Running the password_checker

if __name__ =="__main__":
    password_checker()