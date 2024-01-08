def count_characters(string):
    letters = 0
    digits = 0
    special_symbols = 0
    
    for char in string:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        else:
            special_symbols += 1
            
    return letters, digits, special_symbols

input_string = input("Enter a string: ")
letter_count, digit_count, special_count = count_characters(input_string)

print("Letters:", letter_count)
print("Digits:", digit_count)
print("Special Symbols:", special_count)