def factorial(n):
    if n <= 1: return 1
    return n * factorial(n-1)

for i in range(10):
    print(f"{i}! = {factorial(i)}")
