# Write a funtion to check if a string is a palindrome using string method.

my_string = str(input("Please enter any string:"))

def is_palindrome(s):
    if(s == s[::-1]):
        print(f"{s} is a palindrome.")
    else:
        print(f"{s} is not a palindrome.")

is_palindrome(my_string)