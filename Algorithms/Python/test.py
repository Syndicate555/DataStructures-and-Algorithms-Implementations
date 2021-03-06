import random


def rand(given, new):
    a = random.randint(0, len(given)-1)
    while len(given) != len(new):
        if len(new) == 0:
            new.append(given[a])
        elif given[a] in new:
            a = random.randint(0, len(given) - 1)
        else:
            new.append(given[a])
    return new


print(rand([1, 2, 3], []))
print(rand([1, 2, 3], []))
print(rand([1, 2, 3], []))
