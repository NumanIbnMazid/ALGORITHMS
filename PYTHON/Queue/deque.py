"""
Keywords: Double Ended Queue
Notes:
    - Insertion or Removal of elements can be performed from the front or from the rear.
    - Do not follow FIFO Rule.
Types of Deque:
    - There are two types of Deque:
        * Input restricted Deque
        * Output restricted Deque
"""

class Deque():
    def __init__(self):
        self.queue = []
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def addRear(self, item):
        self.queue.append(item)
    
    def addFront(self, item):
        self.queue.insert(0, item)
    
    def removeRear(self):
        self.queue.pop()
    
    def removeFront(self):
        self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    
dq = Deque()
print(dq.is_empty())
dq.addRear(8)
dq.addRear(5)
dq.addFront(7)
dq.addFront(10)
print(dq.size())
print(dq.is_empty())
dq.addRear(11)
print(dq.removeRear())
print(dq.removeFront())
dq.addFront(55)
dq.addRear(45)
print(dq.queue)
