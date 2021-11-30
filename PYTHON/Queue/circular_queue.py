"""
Keywords: Circular Relation, Extended version of regular queue, Makes use of empty spaces
Time Complexity:
    - O(1)
Workflow:
    - if REAR + 1 == 5 (overflow!), REAR = (REAR + 1)%5 = 0 (start of queue)
"""

class CircularQueue():
    def __init__(self, maxSize):
        self.queue = list()
        self.head = 0
        self.tail = 0
        self.maxSize = maxSize
        
    def __str__(self):
        return str(self.queue)
        
    # Addding elements to the queue
    def enqueue(self, item):
        if self.size() == self.maxSize - 1:
            return ("Queue is full!")
        self.queue.append(item)
        self.tail = (self.tail + 1) % self.maxSize
        return True
    
    # Removing elements from the queue
    def dequeue(self):
        if self.size() == 0:
            return ("Queue is empty!")
        item = self.queue[self.head]
        self.head = (self.head + 1) + self.maxSize
        return item
    
    # Calculating the size of the queue
    def size(self):
        if self.tail >= self.head:
            return (self.tail - self.head)
        return (self.maxSize - (self.head - self.tail))
    
    # display the queue
    def display(self):
        return self.queue
    
    
q = CircularQueue(maxSize=5)
print(q.enqueue(1))
print(q.enqueue(2))
print(q.enqueue(3))
print(q.enqueue(4))
print(q.display())
print(q.enqueue(5))
print(q.display())
print(q.enqueue(6))
print(q.dequeue())
print(q.enqueue(7))
print(q.display())


print("\n * Circular Queue Two * \n")


class CircularQueueTwo():
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.head = self.tail = -1
        
    # insert an element into the circular queue
    def enqueue(self, item):
        if ((self.tail + 1) % self.size == self.head):
            print("The circular queue is full!\n")
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = item
        else:
            self.tail = (self.tail + 1) % self.size
            self.queue[self.tail] = item
            
    # remove an element from the circular queue
    def dequeue(self):
        if self.head == -1:
            print("The circular queue is empty!\n")
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.size
            return temp
    
    # print the circular queue
    def printCircularQueue(self):
        if (self.head == -1):
            print("There are no elements in the circular queue!\n")
        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
            
q2 = CircularQueueTwo(5)
q2.enqueue(1)
q2.enqueue(2)
q2.enqueue(3)
q2.enqueue(4)
q2.enqueue(5)
q2.enqueue(6)
print("Initial queue")
q2.printCircularQueue()
q2.dequeue()
q2.dequeue()
print("Current queue")
q2.printCircularQueue()
