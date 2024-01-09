def greet(name,greeting = "Hello"):
    message = f"{name}...{greeting}"
    return message

name = input("Enter your name: ")
message = greet(name,"Hi")
print(message)
    