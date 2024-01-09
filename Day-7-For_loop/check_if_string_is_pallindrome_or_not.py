def is_palindrome(s):
    s = s.lower()  # Convert to lowercase for case-insensitive comparison
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True

# Example usage:
string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome.")