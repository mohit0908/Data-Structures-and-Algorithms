class Conversion:

	def __init__(self, capacity):
		self.capacity = capacity
		self.top = -1
		# Array used as stack
		self.array = []

		# Operator precedence setting
		self.output = []
		self.precedence = {'+':1, '-':1, '*':2, '/': 2, '^': 3}

	# Check if the stack is empty

	def isEmpty(self):
		if self.top == -1:
			return True
		else:
			return False

	def peek(self):
		return self.array[-1]

	def pop(self):
		if not self.isEmpty():
			self.top -= 1
			return self.array.pop()
		else:
			return '$'

	def push(self, data):
		self.top += 1
		self.array.append(data)

	def isOperand(self, data):
		return data.isalpha()

	# Check if precedence of operator is strictly less than top of stack

	def notGreater(self, i):
		try:
			a = self.precedence[i]
			b = self.precedence[self.peek()]
			return True if a <= b else False
		except KeyError:
			return False

	# Main function to convert infix to postfix expression to postfix expression
	def infixToPostfix(self, exp):
		print(exp)

		# Iterate over expression for conversion
		for i in exp:
			print('Exp:', i, ''.join(self.output))

			# If character is Operand, push to output
			if self.isOperand(i):
				self.output.append(i)
			elif i == '(':
				self.push(i)
			elif i == ')':
				while ((not self.isEmpty() and self.peek() != '(')):
					a = self.pop()
					self.output.append(a)
				if (not self.isEmpty() and self.peek() == '('):
					self.pop()

			# Operator is encountered
			else:
				while((not self.isEmpty() and self.notGreater(i))):
					self.output.append(self.pop())
				self.push(i)

		# pop all operators from stack

		while not self.isEmpty():
			self.output.append(self.pop())

		# Print final output
		print(''.join(self.output))

# Driver program to test above function 
exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = Conversion(len(exp))
obj.infixToPostfix(exp)

# abcd^e-fgh*+^*+i-
