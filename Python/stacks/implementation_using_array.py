# Python program for implementation of stack 
  
# import maxsize from sys module  
# Used to return -infinite when stack is empty 
from sys import maxsize 
  
class Stack:

    def __init__(self):
        self.items = []


    def push(self, data):
        self.items.append(data)

    def pop(self):
        self.items.pop()

    def isEmpty():
        return (self.items ==  [])

    def peek(self):
        return self.items[-1]


if __name__ == '__main__':

    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print('Stack:', stack)