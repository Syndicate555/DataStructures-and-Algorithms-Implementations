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
######################################################################################################################################
# PROBLEM:BRANCH SUMS
# Writeafunctionthattakes in aBinaryTree and returnsalistofitsbranchsumsordered from leftmostbranchsumtorightmostbranchsum.
# A Branchsum is the sum of allvalues in BinaryTreebranch.Abinarytreebranch is apathofnodes in atreethatstartsattherootnode and endsatanyleafnode.
# Each binaryTree node has an integer value, a left child node and a right child node. children nodes can either be BinaryTree nodes themselves or None/null

# SOLUTION:

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

#################################################################################################################
#  PROBLEM: NODEDEPTHS
#  The Distance between a node in a Binary Tree and the Tree's root is called the node's depth
#  Write a function that takes in a Binary Tree and returns the sum of its nodes depths
# Each binaryTree node has an integer value, a left child node and a right child node. children nodes can either be BinaryTree nodes themselves or None/null


def nodeDepths(root, depth=0):
    # Write your code here.
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

 ####################################################################
 # Remove Duplicates from a LinkedList
 ################################################################
 # This is an input class. Do not edit.


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
	temp = linkedList
	while temp is not None:
		nextNode = temp.next
		while nextNode is not None and nextNode.value == temp.value:
			nextNode = nextNode.next
		temp.next = nextNode
		temp = nextNode
    return LinkedList

###############################################
# Reverse a LinkedList
##########################################
class LinkedList:
	def __init__(self,value):
		self.value = value
		self.next = None
def reverseLinkedList(head):
    # Write your code here.
	prev = None
	current = head
	while (current is not None):
		# save the next node
		next = current.next
		# change the direction of the next node to the previous node
		current.next = prev
		
		# change the position of the previous and current nodes
		prev = current
		current = next
	return prev

################################################################
# Binary Search Implementation
################################################################

def binarySearch(array, target):
    # Write your code here.
	return binaryHelper(array, target, 0, len(array)-1)

def binaryHelper(array,target,left,right):
	while left <= right:
		middle = (left + right) // 2
		match = array[middle]
		if target == match:
			return middle
		elif target < match:
			right = middle -1
		else: 
			left = middle +1
	return -1
