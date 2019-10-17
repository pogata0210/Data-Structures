import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack




class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

 
    def insert (self, value):
        
        if value <= self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
                

                
        
   

      
    # Return True if the tree contains the value
    # False if it does not

    def contains (self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
            
            
            """
        if self.value == data:
            return False
        elif self.value > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = BinarySearchTree(data)
                return True
        else:
            self.right = BinarySearchTree(data)
            return True
"""        

"""class root:
    def __init__(self):
        self.root = None

    # Insert the given value into the tree
    def insert(self, data):
        
        if self.root:
            return self.root.insert(data)
        else: 
            self.root= BinarySearchTree(data)
            return True
"""
     
            
"""
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
        
        """
