"""
Keywords: Linear Data Structure, Series of connected nodes
Basic Operations:
    * Traversal: Access each elements of the linked list.
    * Insertion: Add a new element to the linked list.
    * Deletion: Remove an element from the linked list.
    * Search: Find a node in the linked list.
    * Reverse: Reverse the linked list.
    * Sort: Sort the linked list.
"""


# Create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    # Insert after a node
    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Insert at the end
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    # Deleting a node
    def deleteNode(self, position):

        if self.head is None:
            return

        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return

        # Find the key to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        # If the key is not present
        if temp is None:
            return

        if temp.next is None:
            return

        next = temp.next.next

        temp.next = None

        temp.next = next

    # Search an element
    def search(self, key):

        current = self.head

        while current is not None:
            if current.data == key:
                return True

            current = current.next

        return False

    # Sort the linked list
    def sortLinkedList(self, head):
        current = head
        index = Node(None)

        if head is None:
            return
        else:
            while current is not None:
                # index points to the node next to current
                index = current.next

                while index is not None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data

                    index = index.next
                current = current.next

    # Print the linked list
    def printList(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next


if __name__ == '__main__':

    llist = LinkedList()
    llist.insertAtEnd(1)
    llist.insertAtBeginning(2)
    llist.insertAtBeginning(3)
    llist.insertAtEnd(4)
    llist.insertAfter(llist.head.next, 5)

    print('linked list:')
    llist.printList()

    print("\nAfter deleting an element:")
    llist.deleteNode(3)
    llist.printList()

    print()
    item_to_find = 3
    if llist.search(item_to_find):
        print(str(item_to_find) + " is found")
    else:
        print(str(item_to_find) + " is not found")

    llist.sortLinkedList(llist.head)
    print("Sorted List: ")
    llist.printList()



# Second Implementation

class NodeTwo():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedListTwo():
    def __init__(self):
        self.head = None

    # Display the items of Linked List
    def display(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data) + " --> " if itr.next else str(itr.data)
            itr = itr.next

        print(llstr)

    # Get the length of Linked List
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    # Insert item at the beginning of the Linked List
    def insert_at_beginning(self, data):
        node = NodeTwo(data=data, next=self.head)
        self.head = node

    # Insert item at the end of the Linked List
    def insert_at_end(self, data):
        if self.head is None:
            self.head = NodeTwo(data=data, next=None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = NodeTwo(data=data, next=None)

    # Insert item at specific index
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index!")

        if index == 0:
            self.insert_at_beginning(data=data)
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = NodeTwo(data=data, next=itr.next)
                break
            itr = itr.next
            count += 1
    
    # insert a value after a specific value
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        count = 0
        itr = self.head
        is_inserted = False
        while itr:
            if itr.data == data_after:
                itr.next = NodeTwo(data=data_to_insert, next=itr.next)
                is_inserted = True
                break
            itr = itr.next
            count += 1
        
        if not is_inserted:
            print(f"Data After `{data_after}` not found!")

    # Remove an item from specific index
    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index!")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1
    
    # remove a specific value
    def remove_by_value(self, data):
        count = 0
        itr = self.head
        is_removed = False
        while itr:
            # if element is in first index
            if count == 0 and itr.data == data:
                self.head = self.head.next
                is_removed = True
                break
            if itr.next and itr.next.data == data:
                itr.next = itr.next.next
                is_removed = True
                break
            itr = itr.next
            count += 1
        if not is_removed:
            print(f"Data {data} not found!")

    # Insert a list of values in Linked List
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data=data)


if __name__ == '__main__':
    ll = LinkedListTwo()
    print("\n * Linked List Two * \n")
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.insert_at(1, "blueberry")
    ll.remove_at(2)
    ll.display()

    ll.insert_values([45, 7, 12, 567, 99])
    ll.insert_at_end(67)
    ll.display()
    
    # Additional
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.display()
    ll.insert_after_value("grapes", "apple")  # insert apple after mango
    ll.display()
    ll.insert_after_value("banana", "potato")
    ll.display()
    print("* remove operations *")
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.display()
    ll.remove_by_value("figs")
    ll.display()
    ll.remove_by_value("banana")
    ll.display()
    ll.remove_by_value("mango")
    ll.display()
    ll.remove_by_value("apple")
    ll.display()
    ll.remove_by_value("grapes")
    ll.display()
