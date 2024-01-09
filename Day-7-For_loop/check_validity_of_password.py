import re

def is_valid_password(password):
    # Define the criteria: at least 8 characters, containing uppercase, lowercase, digit, and special character
    if len(password) < 8:
        return False
    
    if not re.search("[A-Z]", password):
        return False
    
    if not re.search("[a-z]", password):
        return False
    
    if not re.search("[0-9]", password):
        return False
    
    if not re.search("[!@#$%^&*()-+]", password):
        return False
    
    return True

# Example usage:
password_input = input("Enter your password: ")
if is_valid_password(password_input):
    print("Valid password!")
else:
    print("Invalid password! Please ensure your password is at least 8 characters long and contains uppercase, lowercase, digit, and special character.")