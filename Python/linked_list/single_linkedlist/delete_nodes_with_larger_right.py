class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
class LinkedList:
	def __init__(self):
		self.head = None
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
	def printList(self):
		temp = self.head
		while (temp):
			print(temp.data, end=" ")
			temp = temp.next
		print()


def delete_nodes_with_larger_right(llist):
	current = llist.head
	prev = llist.head
	max = current.data
	while (current is not None):
		if current.data >= max:
			max = current.data
			prev = current
			current = current.next
		else:
			prev.next = current.next
			current.next = None
			current = prev.next
	return

def reverse(llist):
	current = llist.head
	next = None
	prev = None

	while (current is not None):
		next = current.next
		current.next = prev
		prev = current
		current = next
	llist.head = prev

if __name__ == '__main__':
	values_list = [[12, 15, 10, 11, 5, 6, 2, 3], [10, 20, 30, 40, 50, 60], [60, 50, 40, 30, 20, 10]]
	t = len(values_list)
	for index in range(t):
		llist = LinkedList()
		for i in values_list[index]:
			llist.push(i)
		delete_nodes_with_larger_right(llist)
		reverse(llist)
		llist.printList()
		t -= 1
