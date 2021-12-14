# BINARY TREE

# Left Branch
# Right branch
# Every node can have data

# Larger values placed in the right side of the tree
# Smaller values placed in the left side


# Create a binary class
class BinaryTree:
    # Create a constructor
    def __init__(self, value):
        # Assign the data whatever the value it receives
        self.data = value
        #Initialize left and right with None
        self.left = None
        self.right = None

    def insert(self, value):
        if self.data is None:
            self.data = value   
        else:
            # Left = if value is smaller than current data
            if value < self.data:
                # Check if the left branch has value
                if self.left is None:
                    # Assign left branch value an instance 
                    # Assign recursive call 
                    # An object of the BinaryTree
                    self.left = BinaryTree(value)
                else:
                    # Do not modify the left branch, call the insert function instead
                    self.left.insert(value)

            # Right = if values is larger than current data
            elif value > self.data:
                # Check if the left branch has value
                if self.right is None:
                # Assign right branch value an instance 
                # Assign recursive call 
                # An object of the BinaryTree
                    self.right = BinaryTree(value)
                else:
                    # Do not modify the left branch, call the insert function instead
                    self.right.insert(value)

# Create an instance
bt = BinaryTree(100)
bt.insert(90)
bt.insert(105)
print(bt.data)
print('Left', bt.left.data)
print('Right', bt.right.data)
# print(bt.data)
# bt.left = BinaryTree(95)
# bt.right = BinaryTree(150)
# print('Left:', bt.left.data)
# print('Right:', bt.right.data)

