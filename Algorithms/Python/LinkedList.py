class Node(object):
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d


class LinkedList(object):
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, d):
        current_node = self.root
        prev_node = None
        while current_node:
            if current_node.get_data() == d:  # data in the current node
                if prev_node:
                    prev_node.set_next(current_node.get_next())
                else:
                    self.root = current_node.get_next()
                self.size -= 1
                return True  # data removed
            else:  # if the data is not in the current node, you keep traversing through the list

                prev_node = current_node
                current_node = current_node.get_next()
        return False  # data not found

    def find(self, d):  # prints and returns the index of the element in the list and the element itself
        current_node = self.root  # start at the root node
        counter = 0
        while current_node:
            if current_node.get_data() == d:
                print(counter)
                return counter, d
            else:
                current_node = current_node.get_next()
                counter += 1
        return None  # Data not found


# Test operations

testList = LinkedList()
for i in range(10):
    testList.add(i)
    i += 1
testList.remove(6)
testList.find(4)
print("size="+str(testList.get_size()))
