str1 = "Hello, "
str2 = "World!"
result = str1 + str2
# the result will be "Hello, World!"
print(result)

word = "Python"
repeated_word = word * 3
# repeated_word will be "PythonPythonPython"
print(repeated_word)

sentence = "This is a sample sentence."
check1 = "sample" in sentence
check2 = "not" not in sentence
# check1 will be True, check2 will be True
print(check1)
print(check2)

name = "Alice"
age = 30
formatted_str = "My name is %s, and I am %d years old." % (name, age)
print(formatted_str)
# formatted_str will be "My name is Alice, and I am 30 years old."
formatted_str = "My name is {}, and I am {} years old.".format(name, age)
print(formatted_str)
# formatted_str will be "My name is Alice, and I am 30 years old."

str1 = "apple"
str2 = "banana"
result1 = str1 == str2 # False
result2 = str1 < str2 # True (lexicographically, "apple" comes before "banana")
print(result1)
print(result2)


text = "Hello, World!"
index = 0
while index < len(text):
    char = text[index]
    print(char)
    index += 1

