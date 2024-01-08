def reverse_words(string):
    words = string.split()
    reversed_words = words[::-1]
    
    # Reconstruct the string without using join
    reversed_string = ''
    for i in range(len(reversed_words)):
        reversed_string += reversed_words[i]
        if i != len(reversed_words) - 1:
            reversed_string += ' '
    
    return reversed_string

# Example usage
input_string = "Hello World, how are you?"
reversed_string = reverse_words(input_string)
print("Original String:", input_string)
print("Reversed String:", reversed_string)