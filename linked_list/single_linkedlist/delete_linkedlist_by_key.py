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

def delNode(llist, k):
	temp = llist.head

	# if first node contains key then
	if temp.next != None and temp.data == k:
		llist.head = temp.next
		return
	while (temp is not None):
		if temp.data == k:
			break
		prev = temp
		temp = temp.next

	if temp is None:
		return
	prev.next = temp.next

'''
def delNode(head, k):
	temp = head
	# if first node contains key then
	if temp.next != None and temp.data == k:
		head = temp.next
		return head
	while (temp is not None):
		if temp.data == k:
			break
		prev = temp
		temp = temp.next
	if temp is None:
		return head
	prev.next = temp.next
	return head
'''
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
	print('4 node linked list created:', llist.printlist())
	print('Provide key to delete:')
	key = int(input())
	delNode(llist, key)
	llist.printlist()
