class Node:
    def __init__(self, data):
        self.data = data 
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None

    def InsertFirst(self, data):
        NewNode = Node(data)
        if(self.start == None):
            self.start = NewNode
            self.start.prev = self.start
        else:
            NewNode.prev = self.start
            NewNode.next = self.start
            self.start = NewNode

    def InsertLast(self, data):
        newNode = Node(data)
        temp = self.start
        while(temp.next != None):
            temp = temp.next
        temp.next = newNode 
            
    def InsertPos(self, pos,data):
        newNode = Node(data)
        count = 1
        temp = self.start
        while(count != pos):
            count += 1
            temp = temp.next
        newNode.prev = temp
        newNode.next = temp.next
        temp.next = newNode
        temp.next.prev = newNode
    
    def DeleteFirst(self):
        self.start = self.start.next
    
    def DeleteLast(self):
        temp = self.start 
        while(temp.next.next != None):
            temp = temp.next
        temp.next = None

    def DeletePos(self,pos):
        count = 1
        temp = self.start
        while(count != pos-1):
            count+=1
            temp = temp.next
        temp.next = temp.next.next
        temp.next.prev = temp
  
    def PrintList(self):
        temp = self.start
        while(temp!= None):
            print(temp.data, end =" ")
            temp = temp.next
        print()

n1 = LinkedList()
n1.InsertFirst(100)
n1.InsertFirst(200)
n1.InsertFirst(300)
n1.InsertFirst(400)
n1.InsertLast(500)
n1.InsertPos(3,600)
n1.PrintList()
n1.DeletePos(5)
n1.PrintList()