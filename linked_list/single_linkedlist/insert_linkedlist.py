# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
    def printList(self):
        tmp = self.head
        while(tmp):
            print(tmp.data, end=' ')
            tmp=tmp.next
        print()

# Beginning of the list
def insertAtBeginning(head, data):
    # If empty list
    if head == None:
        head = node(data)
        return head
    # If non-empty list
    else:
        temp = head
        head = node(data)
        head.next = temp
        return head

# End of the list
def insertAtEnd(head, data):
    # if empty list
    if head == None:
        head = node(data)
        return head
    else:
        # Traverse till last node
        new_node = node(data)
        temp = head
        while(temp.next):
            temp = temp.next
        temp.next = new_node
        return head

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = Linked_List()
        for e in range(0, len(arr), +2):
            if arr[e+1]==0:
                lis.head = insertAtBeginning(lis.head, arr[e])
            else:
                lis.head = insertAtEnd(lis.head, arr[e])
        lis.printList()