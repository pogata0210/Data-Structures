import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()
        
        #This data structure is FIFO

    def enqueue(self, value): #add value 
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self): #taje a way from last item
        if self.size ==0:
            return
        self.size -=1
        return self.storage.remove_from_head()

    def len(self):
        return self.size