class Queue:
  
  def __init__ (self, size):
    self.front = -1
    self.rear = -1
    self.arr = [0]*size
 
  def isEmpty(self):
    if(self.front == -1 or self.front > self.rear):
      return True
    return False
  
  def isFull(self):
    if(self.front == 0 and self.rear == len(self.arr)-1):
      return True
    return False
    
  def enQueue(self, data):
    if(self.isFull()):
      print("Queue is Overflow ")
      return
      
    if(self.rear == -1):
      self.rear,self.front = 0,0
    else:
      self.rear += 1
  
    self.arr[self.rear] = data
      
    
  def deQueue(self):
    if(self.isEmpty()):
      return 
    temp = self.arr[self.front]
    if(self.rear == 0 and self.front == 0):
      self.rear, self.front == -1,-1
    else:
      self.front += 1
    return temp
    
      
  
  def display(self):
    if(self.isEmpty()):
      print("Queue is empty")
      return
  
    for i in range(self.front,self.rear+1):
      print(self.arr[i], end = " ")  
    print()

  
n = int(input())    
q1 = Queue(n)
q1.enQueue(10)
q1.enQueue(20)
q1.enQueue(30)
print(q1.deQueue())
q1.display()
q1.enQueue(40)
q1.enQueue(50)
q1.display()
q1.deQueue()
q1.deQueue()
q1.deQueue()
q1.deQueue()
q1.deQueue()
# q1.deQueue()
q1.display()
