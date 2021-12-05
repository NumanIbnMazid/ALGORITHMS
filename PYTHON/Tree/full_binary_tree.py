"""
Notes: 
    - Every parent node/internal node has either two or no children.
    - Also known as a proper binary tree.
Full Binary Tree Theorems:
    i = the number of internal nodes
    n = the number of total nodes
    l = the number of leaves
    λ = the number of levels
    
    * The number of leaves:
        -> i + 1
    * The total number of nodes:
        -> 2i + 1
    * The number of internal nodes:
        -> (n - 1) / 2
    * The number of leaves:
        -> (n + 1) / 2
    * The total number of nodes:
        -> 2l - 1
    * The number of internal nodes:
        -> l - 1
    * The number of leaves at most:
        -> 2^λ - 1
"""

# creating node
class Node:
    def __init__(self, item):
        self.item = item
        self.rightChild = None
        self.leftChild = None
        
    
# Checking full binary tree
def isFullTree(root):
    # tree empty case
    if root is None:
        return True
    # checking if child is present
    if root.leftChild is None and root.rightChild is None:
        return True
    if root.leftChild is not None and root.rightChild is not None:
        return (isFullTree(root.leftChild) and isFullTree(root.rightChild))
    

root = Node(1)
root.rightChild = Node(3)
root.leftChild = Node(2)

root.leftChild.leftChild = Node(4)
root.leftChild.rightChild = Node(5)
root.leftChild.rightChild.leftChild = Node(6)
root.leftChild.rightChild.rightChild = Node(7)

if isFullTree(root):
    print("The tree is a full binary tree")
else:
    print("The tree is not a full binary tree")
