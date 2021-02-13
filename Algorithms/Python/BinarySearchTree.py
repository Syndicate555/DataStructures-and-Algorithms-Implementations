class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):  # recursive function to insert an element into the tree
        if self.value == data:  # if the value already exists in the tree, the function returns false
            return False
        elif self.value > data:  # look left of the tree to insert the element since its smaller than the parent node
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)  # if no node exists, create one
                return True
        else:  # look right of the tree to insert the element since its greater than the parent node
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)  # if no node exists, create one
                return True


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:  # if the tree has elements, look through it to figure out the right spot of the element to be inserted
            return self.root.insert(data)
        else:
            # if the tree is empty, start by creating a node
            self.root = Node(data)
            return True
