def generate_fibonacci(limit):
    a, b = 0, 1
    fibonacci_series = []
    while a < limit:
        fibonacci_series.append(a)
        a, b = b, a + b
    return fibonacci_series

# Generating Fibonacci series up to 50
fibonacci_series = generate_fibonacci(50)
print("Fibonacci series up to 50:", fibonacci_series)