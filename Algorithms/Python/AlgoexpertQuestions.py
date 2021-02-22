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

# PROBLEM:BRANCH SUMS
# Writeafunctionthattakes in aBinaryTree and returnsalistofitsbranchsumsordered from leftmostbranchsumtorightmostbranchsum.
# ABranchsum is thesumofallvalues in BinaryTreebranch.Abinarytreebranch is apathofnodes in atreethatstartsattherootnode and endsatanyleafnode.
# Each binaryTree node has an integer value, a left child node and a right child node. children nodes can either be BinaryTree nodes themselves or None/null


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    arr = []
    # Write your code here.
    calculateSums(root, 0, arr)
    return arr

# Helper function to append all the calculated sums to a list


def calculateSums(node, runningSum, arr):
    if node is None:
        return
    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        arr.append(newRunningSum)
        return

    calculateSums(node.left, newRunningSum, arr)
    calculateSums(node.right, newRunningSum, arr)
