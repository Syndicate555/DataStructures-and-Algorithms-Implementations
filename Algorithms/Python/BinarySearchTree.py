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

    def find(self, data):  # recursive function to insert an element into the tree
        if (self.value == data):
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.value))

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()

    def printTree(self):
        if self:
            if self.leftChild:
                self.leftChild.printTree()
            print(self.value)
            if self.rightChild:
                self.rightChild.printTree()

    def invertTree(self):
        left = self.leftChild
        right = self.rightChild
        self.rightChild = left
        self.leftChild = right
        invertTree(self.leftChild)
        invertTree(self.rightChild)


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

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print("This is the Preorder Traversal of the BST")
        self.root.preorder()

    def inorder(self):
        print("This is the Inorder Traversal of the BST")
        self.root.inorder()

    def postorder(self):
        print("This is the Postorder Traversal of the BST")
        self.root.postorder()

    def printTree(self):
        print("Printing the tree")
        self.root.printTree()

    def invertTree(self):
        self.root.invertTree()

# Test Operations


myTree = BST()
myTree.insert(25)
myTree.insert(14)
myTree.insert(35)
myTree.insert(10)
myTree.insert(19)
myTree.insert(31)
myTree.insert(42)
# myTree.inorder()
myTree.printTree()
myTree.invertTree()
myTree.printTree()
# myTree.postorder()
# myTree.preorder()
