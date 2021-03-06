def factorial(n):
    count = 1
    for i in range(1, n+1):
        count = count * i
    return count


print(factorial(4))
