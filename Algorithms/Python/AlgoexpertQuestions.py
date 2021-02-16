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
