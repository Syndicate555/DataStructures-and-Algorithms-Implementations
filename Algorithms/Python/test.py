def getNthFib(n):
    # Write your code here.
    arr = [0, 1]
    for i in range(n-1):
        arr.append(arr[i] + arr[i+1])
    return arr[n-1]


print(getNthFib(2))
