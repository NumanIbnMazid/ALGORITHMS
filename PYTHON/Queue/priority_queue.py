"""
Keywords: Special Type of Queue, Associated with Priority value, 
Terms:
    - 
Basic Operations:
    - insert(x): inserts and element to the priority queue.
    - remove(y): remove an element from the priority queue.
    - peek(): peek and element from the priority queue.
Workflows:
    - Insert:
        * Insert the new element at the end of the tree.
        * Heapify the tree.
    - Removing an element from the queue.
        * Select the element to be removed.
        * Swap it with the last element.
        * Remove the last element.
        * Heapify the tree.
    - Peeking element:
        * Returns the maximum elemnent from the Max Heap or Minimum element from the Min Heap.
Time Complexity:
    - 
Notes:
    - Same priority elements served according to their order in the queue.
    - Highest Value -> Highest Priority / Lowest Value -> Highest Priority / Custom Priority.
    - Element with the Highest Priority is removed first.
    - Can be implemented through: Array, Linked List, Heap, Binary Search Tree.
"""

# Using Queue

class PriorityQueue(object):
    def __init__(self):
        self.queue = list()
        
    def __str__(self):
        return " ".join([str(i) for i in self.queue])
    
    # check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0
    
    # insert element to the queue
    def insert(self, item):
        self.queue.append(item)
        
    # remove element from the queue
    def remove(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()
            
    def size(self):
        return len(self.queue)
    
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert(1)
    pq.insert(2)
    pq.insert(3)
    pq.insert(4)
    pq.insert(5)
    print(pq)
    pq.remove()
    print(pq)
    
    while not pq.is_empty():
        print("Removed: ", pq.remove())
    
    print(pq)