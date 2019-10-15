from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value): #add item to head
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self): # pop items off of a list to remove them, from head
        if self.size ==0:
            return
        self.size -=1
        return self.storage.remove_from_head()

    def len(self):
        return self.size
