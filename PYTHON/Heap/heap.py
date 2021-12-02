"""
Keywords: Complete Binary Tree
Types of Heap:
    * Max Heap
    * Min Heap
Notes:
    * Max Heap: Any given node is always greater than it's child nodes and the key of the root node is the largest among all others.
    * Min Heap: Any given node is always smaller than it's child nodes and the key of the root node is the smallest among all others.
    * Heapify: Process of creating Heap data structure from binary tree. It is used to create Max Heap or Min Heap.
    * Every Parent Node, at most can have only two children.
    * Must be a complete tree. It must be filled from left to right and every level must be full with the exception of the last level not needing to be full.
Basic Operations:
    - Heapify()
    - Insert(x)
    - Delete(y)
    - Peek(z)
    - Find Min/Max
    - Extract Max/Min
Formula:
    - Parent Index: (Index - 1) / 2
    - Left Child Index: 2 * Index + 1
    - Right Child Index: 2 * Index + 2
"""

# Max Heap

class Heap():
    def __init__(self, array=[]):
        self.heap = array
    
    # get parent index of an index
    def get_parent_index(self, index):
        return (index - 1) / 2
    
    # get left child of an index
    def get_left_child_index(self, index):
        return (2 * index) + 1
    
    # get right child of an index
    def get_right_child_index(self, index):
        return (2 * index) + 2
    
    # Heapify the array
    def heapify(self, index):
        largest = index
        left_child_index = self.get_left_child_index(index)
        right_child_index = self.get_right_child_index(index)
        
        if left_child_index < len(self.heap) and self.heap[index] < self.heap[left_child_index]:
            largest = left_child_index
            
        if right_child_index < len(self.heap) and self.heap[index] < self.heap[right_child_index]:
            largest = right_child_index
            
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            # recursive call: heapify the array
            self.heapify(index=largest)
    
    # insert data in the heap array
    def insert(self, new_data):
        # if heap array is empty
        if len(self.heap) == 0:
            self.heap.append(new_data)
        # if heap array is not empty
        else:
            self.heap.append(new_data)
            # heapify the array after inserting
            for i in range((len(self.heap) // 2) - 1, -1, -1):
                self.heapify(index=i)
    
    # delete a node from the heap array
    def delete_node(self, data):
        i = 0
        # loop until the data is found in heap array
        for i in range(0, len(self.heap)):
            if data == self.heap[i]:
                # terminate the loop if the data is found
                break
        
        # swap the target node with the last node of the heap array
        self.heap[i], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[i]
        # remove the data
        self.heap.remove(data)
        # heapify the array
        for index in range((len(self.heap) // 2) - 1, -1, -1):
            self.heapify(index=index)
            
h = Heap(array=[])

h.insert(3)
h.insert(4)
h.insert(9)
h.insert(5)
h.insert(2)

print("Max heap after inserting: ", str(h.heap))

h.delete_node(4)

print("Max heap after deleting: ", str(h.heap))