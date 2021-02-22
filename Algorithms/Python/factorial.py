def factorial(n):
    # recursive implementation
    counter = 0
    if (n <= 0):
        return counter
    factorial(n - 1)


def fact(n):
    # iterative implementation
    counter = 1
    for i in range(1, n+1):
        counter = counter * i
        i += 1
    return counter


print(fact(0))
