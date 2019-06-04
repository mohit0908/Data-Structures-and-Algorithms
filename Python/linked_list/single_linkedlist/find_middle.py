class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def printlist(self):
		temp = self.head
		if self.head == None:
			return
		else:
			while(temp):
				print(temp.data, end = ' ')
				temp = temp.next

def findMid(head):
    len = 0
    temp = head
    # Find length of linked list and position to return
    while (temp is not None):
        len+=1
        temp = temp.next
    pos = int(len/2) + 1
    
    temp = head
    position = 1
    while (temp is not None):
        if position == pos:
            return temp.data
        temp = temp.next
        position += 1


if __name__ == '__main__':

	# Create a linked list
	llist = LinkedList()
	llist.head = Node(1)
	second = Node(6)
	third = Node(3)
	fourth = Node(9)
	llist.head.next = second
	second.next = third
	third.next = fourth
	print('\n4 node linked list created:', llist.printlist())
	m = findMid(llist.head)
	print(m)
