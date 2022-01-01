class Queue:
    def __init__(self, size):
        self.rear = -1
        self.front = -1
        self.arr = [0]*size
    
    def isEmpty(self):
        if(self.front == -1):
            return True
        return False
    
    def isFull(self):
        if (self.front == 0 and self.rear == len(self.arr)-1) or self.front == self.rear+1:
            return True
        return False
    
    def enQueue(self,data):
        if(self.isFull()):
            print("Queue is Full ")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear+1) % len(self.arr)
        self.arr[self.rear] = data

    def deQueue(self):
        if(self.isEmpty()):
            print("Queue is Empty")
            return
        temp = self.arr[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % len(self.arr)
        
    def display(self):
        if(self.isEmpty()):
            print("Queue is empty\n")
            return
        
        last = self.rear + 1 if self.front <= self.rear else len(self.arr)
        for i in range (self.front, last):
            print(self.arr[i], end = " ")
        
        if self.front > self.rear:
            for i in range(0,self.rear+1):
                print(self.arr[i], end= " ")
        print()


n = int(input("Enter size of Queue:\n"))
l1 = Queue(n)
l1.enQueue(10)
l1.enQueue(20)
l1.enQueue(30)
l1.enQueue(40)
l1.deQueue()
l1.display()
l1.enQueue(50)
l1.display()
# l1.deQueue()
# # l1.deQueue()
# # l1.deQueue()
# # l1.deQueue()
# # l1.deQueue()
# l1.display()
# l1.enQueue(50)
# # l1.enQueue(100)
# # l1.enQueue()
# l1.display()