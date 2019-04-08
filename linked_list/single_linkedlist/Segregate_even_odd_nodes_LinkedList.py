    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            return
        node = Node(data)
        node.next = self.head
        self.head = node
    def insert_end(self, data):
        if self.head == None:
            self.head = Node(data)
            return
        # Traverse till last node
        new_node = Node(data)
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_node
    
    def printList(self):
        temp = self.head
        while (temp is not None):
            print(temp.data, end = ' ')
            temp = temp.next
            
def segregate(head):
    # if head is None or list has 1 element
    if head is None or head.next is None:
        print('Single element')
        return head

    temp = head

    # Create 2 LinkedList(for odd and even numbers)
    odd_list = LinkedList()
    even_list = LinkedList()

    # Traverse through linkedlist and insert in the end in odd and evenlist based on node data
    while(temp is not None):
        if temp.data %2 == 0:
            even_list.insert_end(temp.data)
        else:
            odd_list.insert_end(temp.data)
        temp = temp.next

    # If list has only odd/even numbers, return other list head
    if even_list.head is None:
        return odd_list.head
    if odd_list.head is None:
        return even_list.head
    # return even_list

    # If list contains both odd and even numbers: link tail of evenlist to head of oddlist, 
    # Return head of evenlist
    temp = even_list.head
    while (temp.next is not None):
        temp = temp.next
    temp.next = odd_list.head

    return even_list.head
                
if __name__ == '__main__':
    k = int(input())
    for i in range(k):
        llist = LinkedList()
        num = int(input())
        ele = list(map(int, input().split()))
        for index, val in enumerate(ele):
            llist.insert(ele[-index-1])
        llist.head = segregate(llist.head)
        llist.printList()
        print()
        