def minimumWaitingTime(queries):
    # Write your code here.
    time = 0
    arr = []
    queries.sort()
    for i in range(1, len(queries)):
        time += queries[i - 1]
        arr.append(time)

    return sum(arr)


print(minimumWaitingTime([3, 2, 1, 2, 6]))
