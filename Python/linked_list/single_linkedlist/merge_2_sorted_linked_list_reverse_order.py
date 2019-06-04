class Node:

	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	def __init__(self):
		self.head = None

	def insert(self, data):
		if self.head is None:
			self.head = Node(data)
			return
		node = Node(data)
		node.next = self.head
		self.head = node
		return

	def printList(self):
		temp = self.head

		while (temp is not None):
			print(temp.data, end = ' ')
			temp = temp.next
		print()

	def merge_results(self, llist1, llist2):
		temp1 = llist1.head
		temp2 = llist2.head

		# Support function for adding element to linked list
		def add_element(head, data):
			node = Node(data)
			node.next = head
			head = node
			return head
		# If both Linked Lists are empty, return 
		if temp1 is None and temp2 is None:
			self.head = None
			return
		self.head = None

		# Iterate through each element compare, whichever is smaller, append to beginning of third list
		while temp1 is not None or temp2 is not None:
			if temp1 is None and temp2 is not None:
				self.head = add_element(self.head, temp2.data)
				temp2 = temp2.next
			elif temp1 is not None and temp2 is None:
				self.head = add_element(self.head, temp1.data)
				temp1 = temp1.next
			elif temp1 is not None and temp2 is not None:
				if temp1.data < temp2.data:
					self.head = add_element(self.head, temp1.data)
					temp1 = temp1.next
				else: 
					self.head = add_element(self.head, temp2.data)
					temp2 = temp2.next

if __name__ == '__main__':
	values1 = [40,20, 10, 5]
	values2 = [9,7, 4, 2, 1]
	llist1 = LinkedList()
	llist2 = LinkedList()
	llist3 = LinkedList()
	for ele in values1:
		llist1.insert(ele)
	for ele in values2:
		llist2.insert(ele)
	print('Input Lists:')
	llist1.printList()
	llist2.printList()
	llist3.merge_results(llist1, llist2)
	print('Merged list:')
	llist3.printList()