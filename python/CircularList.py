class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__ (self):
        self.start = None
    
    def InsertLast(self, data):
        newNode = Node(data)
        newNode.next = self.start
        if(self.start == None):
            self.start = newNode 
        else:
            temp = self.start
            while(temp.next != self.start):
                temp = temp.next
            temp.next = newNode
              
    def PrintList(self):
        temp = self.start
        print(temp.data)
        while(temp.next != self.start):
            temp = temp.next
            print(temp.data)
       
                
        
            




        
n1 = LinkedList()
n1.InsertLast(10)
n1.InsertLast(20)
n1.PrintList()