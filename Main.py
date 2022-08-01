import os
class Stack:
    #The class is implementing a stack
    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
     #It returns true if the stack is empty and false if the stack is not empty 
        return len(self.items)==0

    def is_full(self):
     #It returns true if the stack is full and false if the stack is not full 
        return len(self.items)==self.size

    def push(self, data):
     #Push data into the stack
        if not self.is_full():
            self.items.append(data)

    def pop(self):
     #Delete a data in the stack 
        if not self.is_empty():
            self.items.pop(-1)

    def status(self):
      #Displays the data in the stack
        for elem in self.items:
             print(elem)

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
