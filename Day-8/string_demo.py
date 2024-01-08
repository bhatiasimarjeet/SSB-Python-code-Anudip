my_single_line_single_quote_string = 'Hi...this is single line single quote string'
print(my_single_line_single_quote_string)

my_single_line_double_quote_string = "Hi...this is single line double quote string"
print(my_single_line_double_quote_string)

my_multi_line_string = '''Hi...this is multi line string
This is second line
This is 3rd line'''
print(my_multi_line_string)

string_hello = "Hello"
print("This is the second character of string hello: ", string_hello[1])

print("This is second last character of string_hello", string_hello[-2])

print("This is first character of string_hello", string_hello[-5])

#Slicing of string_hello
print("This is Sliced string: ", string_hello[1:3])
print("This is another Sliced string: ", string_hello[-4:-1])
print("This is Sliced string: ", string_hello[0:4:2])