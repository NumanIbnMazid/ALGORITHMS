"""
Keywords: Min Heap
"""

# TODO: Bug in Insert Method (Overall not working on the way that the Min Heap Works)

class Heap():
    def __init__(self, array=[]):
        self.heap = array
        
    # get the left child of a index
    def get_left_child_index(self, index):
        return (2 * index) + 1
    
    # get the right child of a index
    def get_right_child_index(self, index):
        return (2 * index) + 2
    
    # Heapify the array
    def heapify(self, index):
        smallest = index
        left_child_index = self.get_left_child_index(index=index)
        right_child_index = self.get_right_child_index(index=index)
        size = len(self.heap)
        
        if left_child_index < size and left_child_index < self.heap[index]:
            smallest = left_child_index
            
        if right_child_index < size and right_child_index < self.heap[index]:
            smallest = right_child_index
        
        # swap if the current index is not smallest among left and right child
        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            # recursive call: heapify the array
            self.heapify(index=smallest)
            
    # insert data in the heap array
    def insert(self, new_data):
        size = len(self.heap)
        if size == 0:
            self.heap.append(new_data)
        else:
            self.heap.append(new_data)
            # heapify the array
            for index in range((size // 2), -1, -1):
                self.heapify(index=index)
                
    # remove data from the heap array
    def delete_node(self, data):
        size = len(self.heap)
        i = 0
        # loop until the data is found in the heap array
        for i in range(0, size):
            if data == self.heap[i]:
                # terminate the loop if the data is found
                break
        # swap the target node with the last node of the heap array
        self.heap[i], self.heap[size - 1] = self.heap[size -1], self.heap[i]
        # remove the data
        self.heap.remove(data)
        # heapify the array
        for index in range((size // 2), -1, -1):
            self.heapify(index=index)


h = Heap(array=[])

h.insert(3)
h.insert(4)
h.insert(9)
h.insert(5)
h.insert(2)

print("Min heap after inserting: ", str(h.heap))

h.delete_node(4)

print("Min heap after deleting: ", str(h.heap))
