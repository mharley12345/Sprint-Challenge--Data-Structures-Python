class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

            #Root occupied when class is instantiated, check whether it is smaller or bigger, respectively goes to left or right
        if(value < self.value):
            if self.left == None: #if there is no leaf, spawn new tree node
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)#otherwise attempt insert from left node as starting node 
        elif(value >= self.value):
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #Start by comparing the target value
        if target < self.value:#If less, check if node is empty, then reached base case and target doesn't exist in the tree
            if self.left is None:
                return False
            return self.left.contains(target)#Otherwise recursion from left node and try finding it
        elif target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
        else:#if target value isn't less or greater, then it found the node
            return True


    # Return the maximum value found in the tree
    def get_max(self): #Go right for maximum value
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()