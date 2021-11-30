"""
Keywords: Linear Data Structure, FIFO
Terms:
    - enqueue: putting items into the queue
    - dequeue: removing items form the queue
Basic Operations:
    - enqueue(x): add an element x to the end of the queue
    - dequeue(): remove an element from the front of the queue
    - isEmpty(): return True if the queue is empty
    - isFull(): return True if the queue is full
    - peek(): return the value of front element of the queue
Time Complexity:
    - enqueue: O(1)
    - dequeue: O(1)
    - dequeue [using pop()]: O(n)
Notes:
    - CPU scheduling, Disk Scheduling uses Queue.
    - When data is transferred asynchronously between two processes.The queue is used for synchronization. For example: IO Buffers, pipes, file IO, etc.
Limitations:
    - After a bit of insertion and deletion, there will be non-usable empty space.
Types of Queue:
    - There are four different types of queues:
        * Simple Queue
        * Circular Queue
        * Priority Queue
        * Double Ended Queue
"""


class Queue:
    def __init__(self):
        self.queue = []
        
    # add an element
    def enqueue(self, item):
        self.queue.append(item)
        
    # check if is empty
    def check_empty(self):
        return len(self.queue) == 0
    
    # removing an element
    def dequeue(self):
        if self.check_empty():
            return None
        return self.queue.pop(0)
    
    # display the queue
    def display(self):
        return self.queue
        
    # show the size of the queue
    def size(self):
        return len(self.queue)
    
q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print("Current queue after enqueue elements: ", q.display())

print("Dequeue: ", q.dequeue())

print("Current queue after dequeue element: ", q.display())

print("Length of Current Queue: ", q.size())