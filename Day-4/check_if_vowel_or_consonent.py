# Accept a single alphabet character from the user
alphabet = input("Enter a single alphabet character: ")
# Check if the alphabet is a vowel or a consonant using a ladder of if-elif-else statements
if alphabet == 'a' or alphabet == 'e' or alphabet == 'i' or alphabet == 'o' or alphabet == 'u':
    print(f"{alphabet} is a vowel.")
else:
    print(f"{alphabet} is a consonant.")