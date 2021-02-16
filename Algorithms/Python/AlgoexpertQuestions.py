def twoNumberSum(array, targetSum):
    # Write your code here.
    # O(n2) time complexity
    arr = []
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if (array[i] + array[j] == targetSum):
                arr.append(array[i])
                arr.append(array[j])
    return arr


def twoNumberSum2(array, targetSum):
    # O(n) time complexity
    nums = {}  # using a HashTable
    arr = []
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            arr.append(potentialMatch)
            arr.append(num)
        else:
            nums[num] = True
    return arr


def isValidSubsequence(array, sequence):
    arrIndex = 0
    seqIndex = 0
    while arrIndex < len(array) and seqIndex < len(sequence):
        if array[arrIndex] == sequence[seqIndex]:
            seqIndex += 1
        arrIndex += 1
        return seqIndex == len(sequence)


def tournamentWinner(competitions, results):
    # Write your code here.
    arr = []
    home = 0
    away = 1
    for i in range(0, len(competitions)):
        if results[i] == 0:
            arr.append(competitions[i][away])
        elif results[i] == 1:
            arr.append(competitions[i][home])
    return max(set(arr), key=arr.count)


tournamentWinner([["HTML", "C#"], ["C#", "Python"],
                  ["Python", "HTML"]], [0, 0, 1])
