"""
Notes:
    - Each node has a maximum of two children.
    - Can be used to search for the presence of a number in O(log(n)) time.
Properties:
    * All nodes of left subtree are less than the root node.
    * All nodes of right subtree are more than the root node.
    * Both subtrees of each node are also Binary Search Tree(BST) i.e. They have the two properties.
Search Operation:
    - If the value is below the root, then we can say for sure that the value is not in right subtree; we need to only search in left subtree and if the value is above the root then we can say for sure that the value is not in left subtree; we need to only search in right subtree.
Insert Operation:
    - We keep going to either right subtree or left subtree depending on the value when we reach a point left or right subtree is null, we put the new node there.
Deletion Operation:
    - Leaf Node Deletion: Simply delete the node from the tree.
    - Node has a single Child Node:
        * Replace that node with it's child node.
        * Remove the child node from it's original position.
    - Node has two children:
        * Get the inorder successor of that node.
        * Replace the node with the inorder successor.
        * Remove the inorder successor from it's original position.
Time Complexity:
        (operation)     (best case)     (average case)      (worst case)
    -   Search          O(log n)        O(log n)            O(n)
    -   Insertion       O(log n)        O(log n)            O(n)
    -   Deletion        O(log n)        O(log n)            O(n)
"""

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
def insert(root, newValue):
    # if binary search tree is empty, make a new node and declare it as root
    if root is None:
        root = BinarySearchTreeNode(newValue)
        return root
    # binary search tree is not empty, so we will insert it into the tree
    # if newValue is less than value of data in root, add it to left subtree and proceed recursively
    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    else:
        # if newValue is greater than value of data in root, add it to right subtree and proceed recursively
        root.rightChild = insert(root.rightChild, newValue)
    return root

def search(root, value):
    if root == None:
        return False
    elif root.data == value:
        return True
    elif root.data < value:
        return search(root.rightChild, value)
    else:
        return search(root.leftChild, value)
    
# Find the inorder successor
def minValueNode(node):
    current = node

    # Find the leftmost leaf
    while(current.leftChild is not None):
        current = current.leftChild

    return current
    
def delete(root, data):
    # return if the tree is empty
    if root is None:
        return root
    # find the node to be deleted
    if data < root.data:
        root.leftChild = delete(root.leftChild, data)
    elif data > root.data:
        root.rightChild = delete(root.rightChild, data)
    else:
        # if the node is with only one child or no child
        if root.leftChild is None:
            temp = root.rightChild
            root = None
            return temp
        elif root.rightChild is None:
            temp = root.leftChild
            root = None
            return temp
        # if the node has two children place the inorder successor in position of the node to be deleted
        temp = minValueNode(root.rightChild)
        root.data = temp.data
        
        # delete the inorder successor
        root.rightChild = delete(root.rightChild, temp.data)
    return root
    
def findLargestElement(root):
    # check if the binary serach tree is empty
    if root is None:
        return False
    elif root.rightChild is None:
        return root.data
    else:
        return findLargestElement(root.rightChild)
    
def findSmallestElement(root):
    # check if the binary search tree is empty
    if root is None:
        return False
    elif root.leftChild is None:
        return root.data
    else:
        return findSmallestElement(root.leftChild)
    
# in-order traversal of the binary search tree
def inorder(root):
    if root is not None:
        # traverse left
        inorder(root.leftChild)
        # traverse root
        print(str(root.data) + " ->", end=' ')
        # traverse right
        inorder(root.rightChild)

# pre-order traversal of the binary search tree
def preorder(root):
    if root is not None:
        # traverse root
        print(str(root.data) + " ->", end=' ')
        # traverse left
        preorder(root.leftChild)
        # traverse right
        preorder(root.rightChild)
        
# post-order traversal of the binary search tree
def postorder(root):
    if root is not None:
        # traverse left
        postorder(root.leftChild)
        # traverse right
        postorder(root.rightChild)
        # traverse root
        print(str(root.data) + " ->", end=' ')
    
    

root = insert(None, 15)
insert(root, 10)
insert(root, 25)
insert(root, 6)
insert(root, 14)
insert(root, 20)
insert(root, 60)
a1 = root
a2 = a1.leftChild
a3 = a1.rightChild
a4 = a2.leftChild
a5 = a2.rightChild
a6 = a3.leftChild
a7 = a3.rightChild
print("Root Node is:")
print(a1.data)
print("left child of node is:")
print(a1.leftChild.data)
print("right child of node is:")
print(a1.rightChild.data)
print("Node is:")
print(a2.data)
print("left child of node is:")
print(a2.leftChild.data)
print("right child of node is:")
print(a2.rightChild.data)
print("Node is:")
print(a3.data)
print("left child of node is:")
print(a3.leftChild.data)
print("right child of node is:")
print(a3.rightChild.data)
print("Node is:")
print(a4.data)
print("left child of node is:")
print(a4.leftChild)
print("right child of node is:")
print(a4.rightChild)
print("Node is:")
print(a5.data)
print("left child of node is:")
print(a5.leftChild)
print("right child of node is:")
print(a5.rightChild)
print("Node is:")
print(a6.data)
print("left child of node is:")
print(a6.leftChild)
print("right child of node is:")
print(a6.rightChild)
print("Node is:")
print(a7.data)
print("left child of node is:")
print(a7.leftChild)
print("right child of node is:")
print(a7.rightChild)
print(search(root,14))
print(search(root,22))
print("Largest Element is:")
print(findLargestElement(root))
print("Smallest Element is:")
print(findSmallestElement(root))
# pre-order traversal
print("pre-order traversal:")
preorder(root=root)
print()
# post-order traversal
print("post-order traversal:")
postorder(root=root)
print()
# in-order traversal
print("in-order traversal:")
inorder(root=root)
print()
root = delete(root, 10)
print("Inorder traversal after deleting: ")
inorder(root)
print()
