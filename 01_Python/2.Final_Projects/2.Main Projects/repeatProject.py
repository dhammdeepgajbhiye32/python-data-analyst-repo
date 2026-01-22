# Here we will repeat the Password Strength Checker Project.

import re

# Condition to check if the password entered is strong or not
# Password must be atleast of 8 characters.
# Password must be contain atleast 1 digit.
# Password must be contain atleast 1 upper-case character.
# Password must be contain atleast 1 lower-case character.
# Password must be contain atleast 1 special-case character.


def password_strength_checker(password):
    if len(password) < 8 :
        return "Weak: The Password needs to be atleast 8 charcters."
    
    if not any(char.isdigit() for char in password):
        return "Weak: The Password needs to be atleast 1 digit."
    
    if not any(char.isupper() for char in password):
        return "Weak: The Password needs to be atleast 1 upper-case character."
    
    if not any(char.islower() for char in password):
        return "Weak: The Password needs to be atleast 1 lower-case character."
    
    if not re.search(r'[~!@#$%^&*(){};:<>,.?/|]',password):
        return "Medium: The Password needs to be atlease 1 special-case character."
    
    return "Strong: The Password is Storng and Secured."

def password_checker():
    print("Welcome to the Password Strength Checker:")

    while True:
        password = input("please enter the password or (type 'exit' to quit).")
        
        if password.lower() == 'exit':
            print("Thankyou for using this tool.")
            break

        result = password_strength_checker(password)
        print(result)

# Running the main execution.

if __name__ == "__main__":
    password_checker()