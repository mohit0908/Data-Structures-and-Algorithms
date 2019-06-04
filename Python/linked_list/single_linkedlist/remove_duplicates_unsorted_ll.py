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
    current = head
    element_list = []
    prev = None
    while (current is not None):
        if current.data not in element_list:
            element_list.append(current.data)
            prev = current
            current = current.next
        else:
            prev.next = current.next
            current = current.next


if __name__ == '__main__':
    values_list = [[5,2,2,4], [2,2,2,2,2]]
    t = len(values_list)
    for index in range(t):
        list1 = Linked_List()
        for i in values_list[index]:
            list1.insert(i)
        print('Input:')
        list1.printlist()
        print()
        removeDuplicates(list1.head)
        print('Output')
        list1.printlist()
        print('')