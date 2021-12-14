
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

    # Insert new data into a binary search tree
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

    # Search for specific data in a binary search tree
    def iter_search(self, node, key):
        # node = self.data
        while node is not None and key != node.data:
            if key < node.data:
                node = node.left
            else:
                node = node.right
        return node.data

    def find_max(self, node):
        if node is None:
            return 0
        node = self.right
        while node.right is not None:
            node = node.right
        return node.data
        
    def find_min(self, node):
        if node is None:
            return 0
        node = self.left
        while node.left is not None:
            node = node.left
        return node.data

    def measure_height(self, node):
        if node is None:
            return -1
        left_height = BinaryTree.measure_height(node.left)
        right_height = BinaryTree.measure_height(node.right)
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

    def delete(self, node, key):
        pass


bst1 = BinaryTree(50)
bst1.insert(49)
bst1.insert(51)
bst1.insert(48)
bst1.insert(1)
bst1.insert(47)
bst1.insert(112)
bst1.insert(109)
bst1.insert(56)
# print(bst1.iter_search(bst1, 47))
# print(bst1.iter_search(bst1, 56))
print('Maximum value:', bst1.find_max(bst1))
print('Minimum value:', bst1.find_min(bst1))

print(bst1.measure_height(bst1))


