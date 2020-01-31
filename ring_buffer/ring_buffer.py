from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #Add new nodes to buffer
        #Nodes cannot exceed capacity, so size of DDLs must be at capacity
        

        #Do this when Buffer is under limit

        if self.storage.length < self.capacity:
        #Check if head is empty to start
            if self.storage.head == None:
                self.storage.add_to_head(item)
                self.current = self.storage.head #To track current node
            else:
            #Add to tail otherwise
                self.storage.add_to_tail(item)
                self.current = self.storage.head
        else:
        #Buffer will become full, need to add items from oldest
        #After it will start adding items at the head (oldest items start)
            if self.current.next == None: #when last item is reached again

                #Update the last item with new item and move pointer back to head, start the process again
                self.current.value = item
                self.current = self.storage.head
                #update position of self.current to the head
            else:#
                self.current.value = item #replace the value and move to next
                #move the current to next node
                self.current = self.current.next
        #Storage capacity will be reached then then will 

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        #Start at head and append until current pointer has nothing 
        current = self.storage.head
        while (current != None):
            list_buffer_contents.append(current.value)
            current = current.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass