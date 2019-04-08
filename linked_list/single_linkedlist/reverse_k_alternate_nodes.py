class LinkedList:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def push(self, value):
        """ Adds a new node to head of list """
        new_node = self.Node(value)
        new_node.next = self.head
        self.head = new_node

    def printLinkedList(self):
        """ Prints all the nodes of a linked list """
        node = self.head
        while node is not None:
            # print(node, node.next)
            print(node.value, end = ' ')
            node = node.next

    def kAltReverse(self, head, k):
        """ Reverses the every k alternate nodes of the list """
        
        current = head
        prev = None
        count = 0


        # Reverse first k nodes
        while (current is not None and count < k):
            current.next, prev, current = prev, current, current.next
            count += 1
        # print('Head:', head, head.next, current)
        # head is now a pointer to (k)th node. Make it point to (k+1)th node
        if head is not None:
            head.next = current
        # print('head again:', head, head.next)

        # Skip k nodes
        count = 0
        while (current is not None and count < k-1):
            current = current.next
            count+= 1

        
        # Recursively call kAltReverse to repeat this process
        if (current is not None):
            current.next = self.kAltReverse(current.next, k)

        return prev


        

if __name__ == '__main__':
    ll = LinkedList()
    for x in range(19, 0, -1):
        ll.push(x)
    reverse_freq = 4

    print("input:", ll.printLinkedList())
    ll.head = ll.kAltReverse(ll.head, reverse_freq)
    print('reversed list:', ll.printLinkedList())