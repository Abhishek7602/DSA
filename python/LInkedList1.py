class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None

    def InsertLast(self, data):
        newNode = Node(data)
        if(self.start == None):
            self.start = newNode
        else:
            temp = self.start
            while(temp.next!= None):
                temp = temp.next
            temp.next = newNode

    def InsertBeg(self, data):
        newNode = Node(data)
        if(self.start == None):
            self.start = newNode
        else:
            newNode.next = self.start
            self.start = newNode
    
    def InsertPostion(self, data, pos):
        count = 1
        newNode = Node(data)
        if(pos == 0):
            newNode.next = self.start
            self.start = newNode
        elif (pos >= 7):
            temp = self.start
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode
        else:
            temp = self.start
            while(count != pos):
                count += 1
                temp = temp.next
            newNode.next = temp.next
            temp.next = newNode

    def DeleteFirst(self):
        if (self.start == None):
            return 
        else:
            self.start = self.start.next
    
    def DeleteEnd(self):
        if (self.start == None):
            return
        else:
            temp = self.start
            while(temp.next.next != None):
                temp = temp.next
            temp.next = None
        
    def DeletePostion(self, Pos):
        count = 1
        temp = self.start
        while(count != Pos-1):
            count += 1
            temp = temp.next
        print(temp.data)
        temp.next = temp.next.next
        
        
    





    
    def NumberOfNode(self):
        count = 0
        temp = self.start
        while(temp != None):
            count +=1
            temp = temp.next
        print(count)
    
    def PrintList(self):
        temp = self.start
        while(temp != None):
            print(temp.data, end=" ")
            temp = temp.next
        print()


n1 = LinkedList()
n1.InsertBeg(1)
n1.InsertLast(5)
n1.InsertLast(10)
n1.InsertBeg(3)
n1.InsertLast(15)
n1.InsertLast(20)
n1.InsertBeg(2)
# n1.NumberOfNode()
n1.InsertPostion(100,6)

n1.PrintList()
n1.DeleteFirst()
n1.PrintList()
n1.DeleteEnd()
n1.PrintList()
n1.DeletePostion(5)
n1.PrintList()



