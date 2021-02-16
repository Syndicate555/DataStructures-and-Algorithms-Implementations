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
    # Write your code here.
    counter = 0
    for i in range(0, len(sequence)):
        for match in array:
            if sequence[i] == match:
                counter += 1
                array.remove(match)
    if counter == len(sequence):
        return True
    else:
        return False
