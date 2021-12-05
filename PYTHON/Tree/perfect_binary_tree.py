"""
Notes:
    - Every internal nodes has exactly two child nodes and all the leaf nodes are in the same level.
    - If a single node has no children, it is a perfect binary tree of height 0.
    - If a node has h > 0, it is a perfect binary tree if both of it's subtrees are height of h - 1 and are non-overlapping.
"""

class Node:
    def __init__(self, k):
        self.key = k
        self.right = self.left = None
        

# calculate depth
def calculateDepth(node):
    d = 0
    while (node is not None):
        d += 1
        node = node.left
    return d

# check if the tree is perfect binary tree
def is_perfect(root, d, level=0):
    # check if the tree is empty
    if (root is None):
        return True
    
    # check the presence if trees
    if (root.left is None and root.right is None):
        return (d == level + 1)
    if (root.left is None or root.right is None):
        return False
    return (
        is_perfect(root.left, d, level + 1) and is_perfect(root.right, d, level + 1)
    )
    

root = None
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

if (is_perfect(root, calculateDepth(root))):
    print("The tree is a perfect binary tree")
else:
    print("The tree is not a perfect binary tree")
