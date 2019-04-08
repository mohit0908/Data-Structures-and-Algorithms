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
            print(temp.data, end = ' ')
            temp = temp.next
        print()

    def move_element(self):
        # If list contains 1 element
        if self.head.next is None:
            return
        temp = self.head

        while temp.next is not None:
            prev = temp
            temp = temp.next
        # detach last element from last-1 element
        prev.next = None
        # attach last element to head
        temp.next = self.head
        # change head position
        self.head = temp 


if __name__ == '__main__':
    values = list(range(10))
    llist = LinkedList()
    for val in values:
        llist.insert(val)
    print('Input list:')
    llist.printList()
    print('Output list')
    llist.move_element()
    llist.printList()