def remove_newline(text):
    text_without_newline = ""
    for char in text:
        if char != '\n':
            text_without_newline += char
    return text_without_newline

# Example usage
text_with_newline = "This is a text\nwith a newline character."
text_without_newline = remove_newline(text_with_newline)
print("Text with newline:", repr(text_with_newline))  # repr() to show special characters
print("Text without newline:", repr(text_without_newline))