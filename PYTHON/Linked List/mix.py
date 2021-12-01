

class NodeTwo():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedListTwo():
    def __init__(self):
        self.head = None
        
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
        
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        
        return count
    
    def insert_at_beginning(self, data):
        node = NodeTwo(data=data, next=self.head)
        self.head = node
        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = NodeTwo(data=data, next=None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
            
        itr.next = NodeTwo(data=data, next=None)
        
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
            
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data=data)
            

if __name__ == '__main__':
    ll = LinkedListTwo()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.insert_at(1, "blueberry")
    ll.remove_at(2)
    ll.display()

    ll.insert_values([45, 7, 12, 567, 99])
    ll.insert_at_end(67)
    ll.display()
