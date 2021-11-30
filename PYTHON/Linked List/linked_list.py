"""
Keywords: Linear Data Structure, Series of connected nodes
Notes:
    - Each node stores data and the address of the next node.
Types of Linked List:
    * Singly Linked List
    * Doubly Linked List
    * Circular Linked List
"""

# Simple Linked List

class Node():
    # Creating a node
    def __init__(self, item):
        self.item = item
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None
        
if __name__ == "__main__":
    linked_list = LinkedList()
    
    # Assigning item values
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    # Connecting Nodes
    linked_list.head.next = second
    second.next = third
    
    # Print the items in linked list
    while linked_list.head != None:
        print(linked_list.head.item)
        linked_list.head = linked_list.head.next