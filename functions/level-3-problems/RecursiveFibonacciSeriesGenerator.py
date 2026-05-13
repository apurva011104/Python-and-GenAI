def generate_fibonacci(n: int):
    if n<=1:
        return n
    return generate_fibonacci(n-1) + generate_fibonacci(n-2)

n = int(input("Enter number: "))

print(generate_fibonacci(n-1))