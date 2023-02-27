def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def print_fibonacci_series(num):
    for i in range(num):
        print(fibonacci(i), end=" ")

print_fibonacci_series(10)
