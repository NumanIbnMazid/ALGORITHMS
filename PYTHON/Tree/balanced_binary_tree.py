"""
Notes:
    - Also referred to as a `Height-Balanced` Binary tree.
    - Height of left and right subtree of any node differ by not more than 1.
Conditions:
    * Difference between the left and right subtree for any node not more than one.
    * The left subtree is balanced.
    * The right subtree is balanced.
"""


class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Height:
    def __init__(self):
        self.height = 0


def isHeightBalanced(root, height):

    left_height = Height()
    right_height = Height()

    if root is None:
        return True

    l = isHeightBalanced(root.left, left_height)
    r = isHeightBalanced(root.right, right_height)

    height.height = max(left_height.height, right_height.height) + 1

    if abs(left_height.height - right_height.height):
        return True