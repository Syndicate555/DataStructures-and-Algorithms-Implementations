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

# isValidSubsequence([1, 1, 1, 1, 1], [1, 1, 1])

a = [1, 2, 3, 4, 5]
dup = a
print(dup)
a.remove(3)
print(dup)
