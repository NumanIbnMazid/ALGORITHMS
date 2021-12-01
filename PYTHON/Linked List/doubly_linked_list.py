"""
Doubly Linked List Components:
    - *prev
    - data
    - *next
Available Insert Positions:
    * Insert at beginning
    * Insert in-between nodes
    * Insert at the end
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # insert item at the beginning of the doubly linked list
    def insert_at_beginning(self, new_data):
        new_node = Node(data=new_data)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    # insert item after a specific node
    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("Previous node cannot be null!")
            return
        
        new_node = Node(data=new_data)
        
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        
        if new_node.next:
            new_node.next.prev = new_node
    
    # insert item at the end of the doubly linked list
    def insert_at_end(self, new_data):
        new_node = Node(data=new_data)
        
        if self.head is None:
            self.head = new_node
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
            
        itr.next = new_node
        new_node.prev = itr
        return
    
    # display the linked list
    def display(self):
        res = ""
        itr = self.head
        while itr:
            data = itr.data
            res += str(data) + " --> " if itr.next else str(data)
            itr = itr.next
            
        print(res)
    
    
# Start with empty list
llist = DoublyLinkedList()

print("\n *** Insert At Beginning *** \n")
llist.insert_at_beginning(7)
llist.insert_at_beginning(10)
llist.insert_at_beginning(16)
llist.insert_at_beginning(11)
llist.display()
print("\n *** Insert After *** \n")
llist.insert_after(llist.head.next, 23)
llist.display()
print("\n *** Insert At End *** \n")
llist.insert_at_end(100)
llist.insert_at_end(200)
llist.insert_at_end(300)
llist.display()

print("\n *** --- *** \n")

# Insert 6. So the list becomes 6->None
llist.insert_at_end(6)

# Insert 7 at the beginning.
# So linked list becomes 7->6->None
llist.insert_at_beginning(7)

# Insert 1 at the beginning.
# So linked list becomes 1->7->6->None
llist.insert_at_beginning(1)

# Insert 4 at the end.
# So linked list becomes 1->7->6->4->None
llist.insert_at_end(4)

# Insert 8, after 7.
# So linked list becomes 1->7->8->6->4->None
llist.insert_after(llist.head.next, 8)

print("Created DLL is: ")
llist.display()
