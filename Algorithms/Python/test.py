def invert(string):
    arr = {}
    for i in range(len(string)):
        arr[string[i]] = ord(string[i])

    sort = sorted(arr.items(), key=lambda x: x[1])
    a = []
    for i in sort:
        a.append(i[0])

    return "".join(a)


print(invert('edcab'))
