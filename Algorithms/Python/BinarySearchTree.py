class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.inset(data)
