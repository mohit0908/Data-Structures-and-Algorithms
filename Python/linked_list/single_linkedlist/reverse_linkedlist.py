'''
Reverse a linked list
Input: 1 2 3 4 5 6
Output: 6 5 4 3 2 1
'''

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def printList(self):
		temp = self.head

		while (temp is not None):
			print(temp.data, end = ' ')
			temp = temp.next
		print()

def reverseList(llist):

	prev = None
	current = llist.head
	next = None

	while (current is not None):
		next = current.next
		current.next = prev
		prev = current
		current = next
	llist.head = prev

if __name__ == '__main__':
	llist = LinkedList()
	llist.head = Node(1)
	second = Node(2)
	third = Node(3)
	four = Node(4)
	llist.head.next = second
	second.next = third
	third.next = four
	print('Actual list:')
	llist.printList()
	print('Reversed:')
	reverseList(llist)
	llist.printList()