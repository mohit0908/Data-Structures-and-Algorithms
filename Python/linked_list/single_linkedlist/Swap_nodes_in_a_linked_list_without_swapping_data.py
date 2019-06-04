import time

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None



class LinkedList:

    def __init__(self):
        self.head = None


    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            self.head = Node(data)
            self.head.next = temp

    def printList(self):
        temp = self.head

        while temp is not None:
            print('Printing:',temp, temp.data)
            temp = temp.next
        print()

    def swap_elements(self, x, y):
            # Nothing to do if x and y are same 
        if x == y:
            return 
  
        # Search for x (keep track of prevX and CurrX) 
        prevX = None
        currX = self.head 
        while currX != None and currX.data != x: 
            prevX = currX 
            currX = currX.next
  
        # Search for y (keep track of prevY and currY) 
        prevY = None
        currY = self.head 
        while currY != None and currY.data != y: 
            prevY = currY 
            currY = currY.next
  
        # If either x or y is not present, nothing to do 
        if currX == None or currY == None: 
            return 
        # If x is not head of linked list 
        if prevX != None: 
            prevX.next = currY 
        else: #make y the new head 
            self.head = currY 
  
        # If y is not head of linked list 
        if prevY != None: 
            prevY.next = currX 
        else: # make x the new head 
            self.head = currX 
  
        # Swap next pointers 
        temp = currX.next
        currX.next = currY.next
        currY.next = temp 





if __name__ == '__main__':
    values = list(range(10))
    llist = LinkedList()
    for val in values:
        llist.insert(val)
    print('Input list:')
    llist.printList()

    llist.swap_elements(6,5)
    llist.printList()