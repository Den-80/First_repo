def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

def number_of_groups(n, k):
    result = factorial(n)/(factorial(n-k)*factorial(k))
    return print(int(result))

print(number_of_groups(50, 7))
