def factorial(n):
    # recursive implementation
    if (n >= 1):
        return n * factorial(n - 1)
    else:
        return 1


def fact(n):
    # iterative implementation
    counter = 1
    for i in range(1, n+1):
        counter = counter * i
        i += 1
    return counter


# Test cases
print(fact(0))
print(factorial(4))
