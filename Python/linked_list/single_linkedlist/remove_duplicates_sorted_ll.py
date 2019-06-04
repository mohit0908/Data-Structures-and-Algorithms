class node:
    def __init__(self):
        self.data = None
        self.next = None
class Linked_List:
    def __init__(self):
        self.head = None
    def get_head(self):
        return self.head
    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node
    def printlist(self):
        temp = self.head
        while temp!=None:
            print(temp.data, end=" ")
            temp= temp.next

def removeDuplicates(head):
    print('function called')
    current = head
    
    while (current is not None and current.next is not None):
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

if __name__ == '__main__':
    t = 1
    for i in range(t):
        list1 = Linked_List()
        values = [1,2,2,3,3,34,5,5,6,7,7]
        for i in values:
            list1.insert(i)
        newHead = None
        list1.printlist()
        removeDuplicates(list1.head)
        list1.printlist()
        print('')
