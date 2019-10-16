from doubly_linked_list import DoublyLinkedList

#there is a capacity inside of a storage


#initiate this method by creating dubmmy header and dummy tail
#DH, DT
#put key  and value of 1
#DH, 1, DT
#put 2 3
#DH, 3, 1, DT
#the recent inserted one goes to the front.

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.current_size = 0
        self.storage = DoublyLinkedList()
        self.dict = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        
        if key in self.dict:
            node = self.dict[key]
            self.storage.move_to_front(node)

            return node.value[1]

        return None
#        current_done = self.storage.head
#        next_node = self.storage.head.next
#       
#        if current_node.key == key:
#           self.sotrage.move_to_end(current_node)

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        
        if key in self.dict:
            node = self.dict[key]
            self.storage.move_to_front(node)
            node.value = (key, value)
            
            return

        if self.current_size == self.limit:
           
            del self.dict[self.storage.tail.value[0]]
            self.storage.remove_from_tail()
            self.current_size -= 1

            self.storage.add_to_head((key, value))
            self.dict[key] = self.storage.head
            self.current_size += 1