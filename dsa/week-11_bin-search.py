
# Write a binary search tree data structure that has these methods:

# Insert new data into a binary search tree
# Search for specific data in a binary search tree
# Determine the Maximum value in the binary search tree
# Determine the Minimum value in the binary search tree
# Determine the Height of the binary search tree (optional, but you'll receive additional points if you answered this correctly)
# Delete a node from a binary search tree (optional, but you'll receive additional points if you answered this correctly)

class BinaryTree:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


    def insert(self, value):
        if self.data is None:
            self.data = value
        else:
            if value < self.data:
                if self.left is None:
                    self.left = BinaryTree(value)
                else:
                    self.left.insert(value)

            elif value > self.data:
                if self.right is None:
                    self.right = BinaryTree(value)
                else:
                    self.right.insert(value)

    def rec_search(self, node, key):
        # node = self.data
        if (node == None or key == node.data):
            return node

        if key < node.data:
            return BinaryTree.rec_search(node.left, key)
        else:
            return BinaryTree.rec_search(node.right, key)
        


    def find_max(self):
        pass

    def find_min(self):
        pass

    def measure_height(self):
        pass

    def delete(self, node, key):
        pass


bst1 = BinaryTree(50)
bst1.insert(49)
bst1.insert(51)
bst1.insert(48)
bst1.insert(47)

print(bst1.rec_search(bst1, 48))


