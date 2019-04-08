class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def insert(self, data):

	    # If empty list
	    if self.head == None:
	        self.head = Node(data)
	    # If non-empty list
	    else:
	        temp = self.head
	        self.head = Node(data)
	        self.head.next = temp

	def printList(self):
		temp = self.head

		while(temp is not None):
			print(temp.data, end = ' ')
			temp = temp.next
		print()


def printList_recursion(head):
	temp = head
	if temp is not None:
		print(temp.data, end = ' ')
		return printList_recursion(temp.next)


if __name__ == '__main__':
	k = list(range(6))

	llist = LinkedList()
	for ele in k:
		llist.insert(ele)
	print('Original list:')
	llist.printList()
	print('Reverse printing using recursion:')
	printList_recursion(llist.head)
	print()