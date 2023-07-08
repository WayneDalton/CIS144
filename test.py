def factorial(n):
    if n <= 1: return 1
    return n * factorial(n-1)

for i in range(11):
    print(f"{i}! = {factorial(i)}")
