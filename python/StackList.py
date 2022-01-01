class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
        
    def isEmpty(self):
      return self.top == None      
    
    def push(self,data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode
        return self.top
        
    def pop(self):
      if self.isEmpty():
        return
      temp = self.top
      self.top = self.top.next
      
    def __displayHelper(self, temp):
      if temp == None:
        return
      self.__displayHelper(temp.next)
      print(temp.data, end=" ")    
      
    def display(self):
      if self.isEmpty():
        print("Stack is empty")
        return
      self.__displayHelper(self.top)
      
      
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.pop()
s1.display()