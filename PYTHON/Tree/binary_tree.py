"""
Keywords: Tree Data Structure
Notes:
    - Each parent node can have at most two children. Each node of a binary tree consists of three items.
        * Data item
        * Address of left child
        * Address of right child
Types of Binary Tree:
    * Full Binary Tree
        - Every parent node/internal nodes has either two or no children.
    * Perfect Binary Tree
        - Every internal nodes has exactly two child nodes and all the leaf nodes are at the same level.
    * Complete Binary Tree
        - Just like full binary tree with two major differences.
        - Every level must be completely filled.
        - All the leaf elements must lean towards the left.
        - The last leaf element might not have a right sibling i.e. a complete binary tree doesn't have to be a full binary tree.
    * Degenerate or Pathological Tree
        - Having a single child either left or right.
    * Skewed Binary Tree
        - Pathological/Degenerate tree in which the tree is either dominated by the left nodes or the right nodes. Thus there are two types of kkewed binary tree.
            - Left skewed binary tree
            - Right skewed binary tree
    * Balanced Binary Tree
        - Difference between the height of the left and right subtree for each node is either 0 or 1.
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
    # traverse in preorder
    def traversePreorder(self):
        print(str(self.val) + " -->", end="")
        if self.left:
            self.left.traversePreorder()
        if self.right:
            self.right.traversePreorder()
            
    # traverse in inorder
    def traverseInorder(self):
        if self.left:
            self.left.traverseInorder()
        print(str(self.val) + " -->", end="")
        if self.right:
            self.right.traverseInorder()
            
    # traverse in postorder
    def traversePostorder(self):
        if self.left:
            self.left.traversePostorder()
        if self.right:
            self.right.traversePostorder()
        print(str(self.val) + " -->", end="")


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)

print("Pre order Traversal: ", end="")
root.traversePreorder()
print("\nIn order Traversal: ", end="")
root.traverseInorder()
print("\nPost order Traversal: ", end="")
root.traversePostorder()
